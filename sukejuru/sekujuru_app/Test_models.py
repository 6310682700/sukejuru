from django.test import TestCase, client
from .models import AnimePlatforms, Genres, Seasons, Days, Anime, Users, Favorite
from django.urls import reverse 
from django.contrib.auth.models import User

class testModel(TestCase):

    def setUp(self):
        User.objects.create(username = "non")
        AnimePlatforms.objects.create(name = "phone")
        Days.objects.create(name = "Monday")
        Genres.objects.create(name ="Fantasy")
        Seasons.objects.create(season = "Winter")
        Anime.objects.create(anime_name ="A", anime_id = "1", rating = 5, platform = "phone")
        Anime.objects.first().day.set("Monday")
        Anime.objects.first().genre.set("Fantasy")
        Anime.objects.first().season.set("Winter")
        Users.objects.create(fav_anime = Anime.objects.first(), d_user = User.objects.first())
        Favorite.objects.create(user = Users.objects.first())
    
    def test_anime_platform(self):
        Platform = Anime.objects.first()
        self.assertEqual(Platform.platform, "phone")