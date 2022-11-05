from django.test import TestCase, client
from .models import anime_platforms, genre ,season, Anime, Users, Favorite
from django.urls import reverse 
from django.contrib.auth.models import User

class testModel(TestCase):

    def setUp(self):
        User.objects.create(username = "non")
        Anime.objects.create(anime_name ="A",anime_id = "1",MONDAY = True, TUESDAY = False,WEDNESDAY = False, THURSDAY = False, FRIDAY = False,SATURDAY = False,
        SUNDAY = False, anime_genre = "AAA", rating = 5, platform = "phone" , anime_season = "winter")
        anime_platforms.objects.create(name = "phone")
        genre.objects.create(type ="AAA")
        Users.objects.create(fav_anime = Anime.object.first, d_user = User.object.first)
        season.objects.create(name = "winter")
        Favorite.objects.create(user = User.objects.first)
    
    def test_anime_on_monday(self):
        Anime = Anime.objects.first()
        self.assertEqual(Anime.MONDAY, True)

    def test_anime_on_tuesday(self):
        Anime = Anime.objects.first()
        self.assertEqual(Anime.TUESDAY, True)

    def test_anime_platform(self):
        Platform = Anime.objects.first
        self.assertEqual(Platform.platform, "phone")

    def test_anime_season(self):
        Season = Anime.objects.first
        self.assertEqual(Season.anime_season, "winter")