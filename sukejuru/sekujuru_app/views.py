from re import template
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from audioop import reverse
from cgitb import html
from email import message
from re import sub
import re
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import AnimePlatform, Genre, Season, Day, Anime, WebUser, Favorite
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
    return render(request, 'User/home.html', {
        'message': 'See you later'
    })

def home_view(request):
    anime_list = Anime.objects.all()
    
    return render(request, 'Home/home.html', {
        'Anime_list': anime_list
    })