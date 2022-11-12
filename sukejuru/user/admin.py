from django.contrib import admin
from .models import WebUser, Favorite

# Register your models here.
admin.site.register(WebUser)
admin.site.register(Favorite)