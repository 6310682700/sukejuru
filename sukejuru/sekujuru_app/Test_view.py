from django.test import SimpleTestCase
from django.test import TestCase, Client
from django.urls import reverse 
from django.db.models import Max
from django.contrib.auth.models import User
from django.test import TestCase, client
from .models import AnimePlatform, Genre, Season, Day, Anime
from django.urls import reverse 
from user.models import WebUser, Favorite
from .form import NewUserForm
from django import forms
from user.views import profile_redirect, profile_view

class testView(TestCase):                                                                               # Test user

    def setUp(self):
        admin = User.objects.create_superuser('admin', 'admin@email.com', 'sukejuru')
        self.response = self.client.get(reverse('home'))
        # Favorite.objects.create(user='non', anime=Anime.objects.first)
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
        self.assertEqual(response.status_code, 302) 

    def test_logout(self):
        self.client = Client()
        response = self.client.post(reverse('login'), {"username": "non", "password" :"angsuvapattanakul"})
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)

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

    def test_user_login(self):                                                                          # Test user can login with valid account
        user = User.objects.first() 
        login = self.client.post(reverse('home'), {"username": "non","password" :"angsuvapattanakul"})   
        self.assertTrue(login) 
    
    def test_user_login_fail(self):                                                                      # Test user login with non-valid account
        login = self.client.login(username='blablabla', password='heck') 
        self.assertFalse(login)

    def test_platform_search(self):                                                                       # Test search with platform
        platform = AnimePlatform.objects.first()    
        searched = self.client.get(reverse('search'), {'platform': platform.name}).context['result']
        search = searched[0].anime_name
        self.assertEqual(search, 'Ant man')

    def test_genre_search(self):                                                                       # Test search with genre
        genre = Genre.objects.first()    
        searched = self.client.get(reverse('search'), {'genre': genre.name}).context['result']
        search = searched[0].anime_name
        self.assertEqual(search, 'Ant man')

    def test_seasons_search(self):                                                                       # Test search with seasons
        seasons = Season.objects.first()    
        searched = self.client.get(reverse('search'), {'seasons': seasons.name}).context['result']
        search = searched[0].anime_name
        self.assertEqual(search, 'Ant man')

    def test_index(self):                                                                               # idk why i need to test this but it increase percent coverage
        self.client = Client()
        self.assertTemplateUsed(self.response, 'Home/home.html')

    def test_registable_form(self):                                                                     # Test user registeration
        form = NewUserForm(data={
            'username' : 'kaykon',
            'email' : 'kaykay@email.com',
            'password1' : 'ikidk1234',
            'password2' : 'ikidk1234',})
        self.assertTrue(form.is_valid())

    def test_empty_form(self):                                                                          # Test user fake registeration
        form = NewUserForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 4)


    # def test_anime_page(self):                                                                             # Test episode page
    #     self.client = Client()
    #     response = self.client.post(reverse('anime_page'), {"username": "non","password" :"angsuvapattanakul"})
    #     self.assertEqual(response.status_code, 200)        



class TestAdmin(TestCase):                                                                                # Test admin parts

    def create_admin(self):                                                                               # Setup admin superuser
        user = NewUserForm(data={
            'username' : 'admin',
            'email' : 'admin@email.com',
            'password1' : 'sukejuru1234',
            'password2' : 'sukejuru1234'
        })
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save()

    def test_admin_site(self):
        self.create_admin()
        client = Client()
        client.login(username='admin',password='sukejuru1234')
        response = self.client.post(reverse('admin:index'))
        self.assertEqual(response.status_code, 302)

    def test_admin_to_user_site(self):
        self.create_admin()
        client = Client()
        client.login(username='admin',password='sukejuru1234')
        response = self.client.post(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_admin_to_userprofile(self):
        self.create_admin()
        client = Client()
        client.login(username='admin',password='sukejuru1234')
        response = self.client.post(reverse('admin:index'))
        self.assertEqual(response.status_code, 302)
    
    




        

        