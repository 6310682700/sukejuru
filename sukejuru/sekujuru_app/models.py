from django.db import models
from django.contrib.auth.models import User

# ที่ทำ class platform, genre และ season เพราะจะได้เรียงตามพวกนี้ละก็ใส่ได้หลายอันได้
class anime_platforms(models.Model):
    name = models.CharField(max_length=99)

class genre(models.Model):
    type = models.CharField(max_length=99)

class season(models.Model):
    name = models.CharField(max_length=99)

class Anime(models.Model):
    anime_id = models.IntegerField(primary_key=True)
    anime_name = models.CharField(max_length=99)
    description = models.CharField(max_length=999)
    platform = models.ManyToManyField(anime_platforms)
    # ที่ใข้แยกทีละอันเพราะจะได้สามารถใส่ anime ที่ออกอากาศ 2 วันต่ออาทิตย์ได้
    MONDAY = models.BooleanField()
    TUESDAY = models.BooleanField()
    WEDNESDAY = models.BooleanField()
    THURSDAY = models.BooleanField()
    FRIDAY = models.BooleanField()
    SATURDAY = models.BooleanField()
    SUNDAY = models.BooleanField()
    time = models.TimeField()
    anime_genre = models.ManyToManyField(genre)
    anime_season = models.ManyToManyField(season)
    rating = models.IntegerField()
 
class Users(models.Model):
    fav_anime = models.ManyToManyField(Anime, blank=True, through='Favorite')
    d_user = models.ForeignKey(User, on_delete=models.CASCADE)

class Favorite(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)

    class Mete:
        unique_together = [['user', 'anime']]