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
        Seasons.objects.create(name = "Winter")
        Anime.objects.create(anime_name ="A", anime_id = "1", time= "09:00", rating = 5)
        Anime.objects.first().day.add(Days.objects.get(id=1))
        Anime.objects.first().genre.set("1")
        Anime.objects.first().season.set("1")
        Anime.objects.first().platform.set("1")
        Users.objects.create(d_user = User.objects.first())
        Users.objects.first().fav_anime.set("1")
    
    def test_anime_platform(self):
        Platform = Anime.objects.first()
        self.assertEqual(Platform.day.get(name = 'Monday').name, "Monday")