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


# Create your views here.

def index(request):
    if request.user.is_superuser:
        return HttpResponseRedirect(reverse('admin:index'))
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    return render(request, 'home.html', {
    }) 

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))            
        else:
            return render(request, 'login.html', {
                'message': 'invalid username or password.'
                })
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return render(request, 'login.html', {
        'message': 'See you later'
    })

def home_view(request):
    anime_list = Anime.objects.all()
    
    return render(request, 'home.html', {
        'Anime_list': anime_list
    })