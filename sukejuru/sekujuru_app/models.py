from django.db import models
from django.contrib.auth.models import User

# ที่ทำ class platform, genre และ season เพราะจะได้เรียงตามพวกนี้ละก็ใส่ได้หลายอันได้
class AnimePlatforms(models.Model):
    name = models.CharField(max_length=99)

    def __str__(self):
        return f'{self.name}'

class Genres(models.Model):
    name = models.CharField(max_length=99)

    def __str__(self):
        return f'{self.name}'

class Seasons(models.Model):
    name = models.CharField(max_length=99)

    def __str__(self):
        return f'{self.name}'

class Days(models.Model):
    name = models.CharField(max_length=99)
    
    def __str__(self):
        return f'{self.name}'
    

class Anime(models.Model):
    anime_id = models.IntegerField(primary_key=True)
    anime_name = models.CharField(max_length=99)
    description = models.CharField(max_length=999)
    platform = models.ManyToManyField(AnimePlatforms)
    day = models.ManyToManyField(Days)
    time = models.TimeField()
    genre = models.ManyToManyField(Genres)
    season = models.ManyToManyField(Seasons)
    rating = models.IntegerField()

    def __str__(self):
        return f'{self.anime_id}: {self.anime_name} {self.description} {self.platform} {self.day} {self.time} {self.genre} {self.season} {self.rating}'
    
 
class Users(models.Model):
    fav_anime = models.ManyToManyField(Anime, blank=True, through='Favorite')
    d_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.d_user}: {self.fav_anime}'

class Favorite(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}: {self.anime}'

    class Meta:
        unique_together = [['user', 'anime']]