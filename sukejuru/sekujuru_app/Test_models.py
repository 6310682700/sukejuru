from django.test import TestCase, client
from .models import AnimePlatform, Genre, Season, Day, Anime
from django.urls import reverse 
from django.contrib.auth.models import User
from user.models import WebUser, Favorite

class testModel(TestCase):

    def setUp(self):
        User.objects.create(username = "non")
        AnimePlatform.objects.create(name = "phone")
        AnimePlatform.objects.create(name = "netflix")
        Day.objects.create(name = "Monday")
        Day.objects.create(name = "Friday")
        Genre.objects.create(name ="Fantasy")
        Season.objects.create(name = "Winter")
        Anime.objects.create(anime_name ="A", anime_id = "1", time= "09:00", rating = 5)
        Anime.objects.first().day.add(Day.objects.get(id=1))
        Anime.objects.first().day.add(Day.objects.get(id=2))
        Anime.objects.first().genre.set(Genre.objects.all())
        Anime.objects.first().season.set(Season.objects.all())
        Anime.objects.first().platform.add(AnimePlatform.objects.get(id=1))
        Anime.objects.first().platform.add(AnimePlatform.objects.get(id=2))
        WebUser.objects.create(d_user = User.objects.first())
        WebUser.objects.first().fav_anime.set(Anime.objects.all()) 
    
    def test_anime_platform(self):
        animes = Anime.objects.first()

        self.assertEqual(animes.platform.get(name = 'phone').name, "phone")

    def test_anime_day(self):
        day = Anime.objects.first()
        self.assertEqual(day.day.get(name = 'Monday').name, 'Monday')

    def test_anime_non_day(self):
        nonday = Anime.objects.first()
        nonday = list(dict(nonday.day.all().values_list()).values())
        self.assertFalse('Tuesday' in nonday)

    def test_anime_seasons(self):
        seasons = Anime.objects.first()
        self.assertEqual(seasons.season.get(pk = 1).name, 'Winter')
