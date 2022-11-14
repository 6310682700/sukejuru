from ast import arg
from django.test import TestCase, Client
from django.urls import reverse 
from django.db.models import Max
from django.contrib.auth.models import User
from django.test import TestCase, client
from .models import AnimePlatform, Genre, Season, Day, Anime
from django.urls import reverse 
from user.models import WebUser, Favorite


class testView(TestCase):

    def setUp(self):
        User.objects.create(username = "non", password = "angsuvapattanakul")
        AnimePlatform.objects.create(name = "phone")
        AnimePlatform.objects.create(name = "netflix")
        Day.objects.create(name = "Monday")
        Genre.objects.create(name ="Fantasy")
        Season.objects.create(name = "Winter")
        Anime.objects.create(anime_name ="Ant man", anime_id = "1", time= "09:00", rating = 5)
        Anime.objects.first().day.add(Day.objects.get(id=1))
        Anime.objects.first().genre.set(Genre.objects.all())
        Anime.objects.first().season.set(Season.objects.all())
        Anime.objects.first().platform.add(AnimePlatform.objects.get(id=1))
        Anime.objects.first().platform.add(AnimePlatform.objects.get(id=2))
        WebUser.objects.create(d_user = User.objects.first())
        WebUser.objects.first().fav_anime.set(Anime.objects.all()) 
    
    def test_login(self):                                                                           # Test page is availible
        self.client = Client()                                
        response = self.client.post(reverse('login'), {"username": "non","password" :"angsuvapattanakul"})
        self.assertEqual(response.status_code, 200) 

    def test_logout(self):
        self.client = Client()
        response = self.client.post(reverse('login'), {"username": "non", "password" :"angsuvapattanakul"})
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 200)

    def test_user_homepage(self):
        self.client = Client()
        response = self.client.post(reverse('home'), {"username": "non","password" :"angsuvapattanakul"})
        self.assertEqual(response.status_code, 200)

    def test_user_about(self):
        self.client = Client()
        response = self.client.post(reverse('about'), {"username": "non","password" :"angsuvapattanakul"})
        self.assertEqual(response.status_code, 200)

    def test_user_search(self):
        self.client = Client()
        response = self.client.post(reverse('search'), {"username": "non","password" :"angsuvapattanakul"})
        self.assertEqual(response.status_code, 200)

    def test_user_regist(self):                                                                          # Test user can register
        self.client = Client()
        response = self.client.post(reverse('register'), {"username": "non","password" :"angsuvapattanakul"})
        self.assertEqual(response.status_code, 200)            

    def test_user_login(self):
        user = User.objects.first() 
        login = self.client.post(reverse('home'), {"username": "non","password" :"angsuvapattanakul"})   # Test user can login with valid account
        self.assertTrue(login) 
    
    def test_user_login_fail(self):                                                                      # Test user login with non-valid account
        login = self.client.login(username='blablabla', password='heck') 
        self.assertFalse(login)

    def test_search(self):
        platform = AnimePlatform.objects.first()    
        searched = self.client.get(reverse('search'), {'platform': platform.name}).context['result']
        search = searched[0].anime_name
        self.assertEqual(search, 'Ant man')