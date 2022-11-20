from django.http import HttpResponse
from django.shortcuts import render
from audioop import reverse
import datetime
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *
from .form import NewUserForm
from user.models import WebUser, Favorite
from django.db.models import Q
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def index(request):
    return HttpResponseRedirect(reverse('home'))

def register_view(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
    else:
        form = NewUserForm()
    return render(request=request, template_name='User/register.html', context={'register_form':form})

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if request.user.is_superuser:
                return HttpResponseRedirect(reverse('admin:index'))
            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponseRedirect(reverse('home'))
            # return render(request, 'Home/home.html', {
            #     'message': 'invalid username or password.'
            #     })
    return HttpResponseRedirect(reverse('home'))

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


def home_view(request):
    anime_list = Anime.objects.all().order_by("-rating")
    fav_ani = None
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user)
        try:
            fav_ani = WebUser.objects.get(d_user=user).fav_anime.all()
        except:
            fav_ani = None

    return render(request, 'Home/home.html', {
        'anime_list': anime_list,
        'fav_list' : fav_ani,
    })


def do_favorite(request):
    if request.method == "POST":
        data = request.POST['data']
        anime = Anime.objects.get(anime_name=data)
        user = WebUser.objects.get(d_user=User.objects.get(username=request.user.username))
        user.fav_anime.add(anime)
        
    return HttpResponseRedirect(reverse('home'))

def remove_favorite(request):
    if request.method == "POST":
        data = request.POST['data']
        anime = Anime.objects.get(anime_name=data)
        user = WebUser.objects.get(d_user=User.objects.get(username=request.user.username))
        user.fav_anime.remove(anime)
        
    return HttpResponseRedirect(reverse('home'))

def calender_view(request):
    if request.method == "GET":
        request_day = request.GET.get("day")

        if request_day=="All" or request_day==None:
            anime = Anime.objects.all()
        else:
            anime = Anime.objects.filter(day__name=request_day)
        
        day_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        x = datetime.datetime.today().weekday()
        anime_today = Anime.objects.filter(day__name=day_of_week[x], time__gte=datetime.datetime.now().strftime("%H:%M:%S")).order_by('time').first()

        print(anime_today)

        context = {
            "Anime": anime,
            "Anime_today": anime_today
        }

        return render(request, 'Home/calender.html', context)
        
def about_view(request):
    return render(request, 'Home/about.html', {
    })

def search_view(request):
    context = {
        "platform": AnimePlatform.objects.all(),
        "genre": Genre.objects.all(),
        "season": Season.objects.all(),
    }
    if request.method == "GET":
        query = request.GET.get("q")
        platform = request.GET.get("platform")
        genre = request.GET.get("genre")
        season = request.GET.get("season")
        rating = request.GET.get("rating")
        day = request.GET.get("day")

        if query==None:            
            search_result = Anime.objects.all().order_by("-rating")
            context.update({"result": search_result})
        else:
            search_result = Anime.objects.filter(
                Q(anime_name__icontains=query) | Q(description__icontains=query), 
            )

        if platform != "All" and platform != None:
            search_result = search_result.filter(platform__name=platform)

        if genre != "All" and genre != None:
            search_result = search_result.filter(genre__name=genre)

        if season != "All" and season != None:
            search_result = search_result.filter(season__name=season)

        if rating != "All" and rating != None:
            search_result = search_result.filter(rating=int(rating))

        if day != "All" and day != None:
            search_result = search_result.filter(day__name=day)

        context.update({"result": search_result})

    return render(request, 'Home/search.html', context)

def anime_page(request, id):    
    anime = Anime.objects.get(anime_id=id)
    episode = None
    if request.method == "GET":
        platform = request.GET.get("platform")        
        try:
            episode = Episode.objects.filter(anime_id=id, platform_id=AnimePlatform.objects.get(name=platform).id)
        except:            
            episode = Episode.objects.filter(anime_id=id, platform_id=AnimePlatform.objects.all().first().id)
    
    context = {
        "anime": anime,        
        "platform": AnimePlatform.objects.all(),
        "genre": Genre.objects.filter(anime=id),
        "season": Season.objects.filter(anime=id),
        "episode": episode,
    }
    return render(request, 'Home/anime_page.html', context)