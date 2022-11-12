from re import template
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from audioop import reverse
from cgitb import html
from email import message
from re import sub
import datetime
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import AnimePlatform, Genre, Season, Day, Anime
from .form import NewUserForm


# Create your views here.

def index(request):
    if request.user.is_superuser:
        return HttpResponseRedirect(reverse('admin:index'))
    # if not request.user.is_authenticated:
    #     return HttpResponseRedirect(reverse('login'))
    return render(request, 'Home/home.html', {
    }) 

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
            return HttpResponseRedirect(reverse('index'))            
        else:
            return render(request, 'User/login.html', {
                'message': 'invalid username or password.'
                })
    return render(request, 'User/login.html')

def logout_view(request):
    logout(request)
    return render(request, 'Home/home.html', {
        'message': 'See you later'
    })

def home_view(request):
    anime_list = Anime.objects.all()
    
    return render(request, 'Home/home.html', {
        'Anime_list': anime_list
    })

def calender(request):
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

<<<<<<< HEAD
    return render(request, 'Home/calender.html', context)
=======
        return render(request, 'Home/calender.html', context)
        
def about_view(request):
    return render(request, 'Home/about.html', {
    })
>>>>>>> 57992945b33a1c6666d322f0ce9d30b74f9e286e
