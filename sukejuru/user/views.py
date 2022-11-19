from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout, admin
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def profile_redirect(request):
    if request.user.is_superuser:
        return HttpResponseRedirect(reverse('admin:index'))
    return HttpResponseRedirect(reverse('profile'))

def profile_view(request):
    pass