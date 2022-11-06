from django.contrib import admin

from .models import AnimePlatform, Genre, Season, Day, Anime, WebUser, Favorite

# Register your models here.

admin.site.register(Anime)
admin.site.register(WebUser)
admin.site.register(Favorite)
admin.site.register(AnimePlatform)
admin.site.register(Genre)
admin.site.register(Season)
admin.site.register(Day)