from ast import arg
from django.test import TestCase, Client
from django.urls import reverse 
from django.db.models import Max
from django.contrib.auth.models import User
from django.test import TestCase, client
from .models import AnimePlatform, Genre, Season, Day, Anime, WebUser, Favorite
from django.urls import reverse 

class testView(TestCase):

    def setUp(self):
        User.objects.create(username = "non", password = "ang")
        AnimePlatform.objects.create(name = "phone")
        AnimePlatform.objects.create(name = "netflix")
        Day.objects.create(name = "Monday")
        Genre.objects.create(name ="Fantasy")
        Season.objects.create(name = "Winter")
        Anime.objects.create(anime_name ="A", anime_id = "1", time= "09:00", rating = 5)
        Anime.objects.first().day.add(Day.objects.get(id=1))
        Anime.objects.first().genre.set(Genre.objects.all())
        Anime.objects.first().season.set(Season.objects.all())
        Anime.objects.first().platform.add(AnimePlatform.objects.get(id=1))
        Anime.objects.first().platform.add(AnimePlatform.objects.get(id=2))
        WebUser.objects.create(d_user = User.objects.first())
        WebUser.objects.first().fav_anime.set(Anime.objects.all())
    

    def test_login(self):
        self.client = Client()
        response = self.client.post(reverse('login'), {"username": "non","password" :"ang"})
        self.assertEqual(response.status_code, 200)
        

    def test_logout(self):
        self.client = Client()
        response = self.client.post(reverse('login'), {"username": "non", "password" :"ang"})
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 200)

    def test_user_homepage(self):
        self.client = Client()
        response = self.client.post(reverse('home'), {"username": "non","password" :"ang"})
        self.assertEqual(response.status_code, 200)