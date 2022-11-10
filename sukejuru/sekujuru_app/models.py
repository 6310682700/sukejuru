from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# สร้าง WebUser object เมื่อมีการ create user
@receiver(post_save, sender=User)
def create_user_picks(sender, instance, created, **kwargs):
    if created:
        WebUser.objects.create(d_user=instance)

# ที่ทำ class platform, genre และ season เพราะจะได้เรียงตามพวกนี้ละก็ใส่ได้หลายอันได้
class AnimePlatform(models.Model):
    name = models.CharField(max_length=99)

    def __str__(self):
        return f'{self.name}'

class Genre(models.Model):
    name = models.CharField(max_length=99)

    def __str__(self):
        return f'{self.name}'

class Season(models.Model):
    name = models.CharField(max_length=99)

    def __str__(self):
        return f'{self.name}'

class Day(models.Model):
    name = models.CharField(max_length=99)
    
    def __str__(self):
        return f'{self.name}'
    

class Anime(models.Model):
    anime_id = models.IntegerField(primary_key=True)
    anime_name = models.CharField(max_length=99)
    description = models.CharField(max_length=999)
    platform = models.ManyToManyField(AnimePlatform)
    day = models.ManyToManyField(Day)
    time = models.TimeField()
    genre = models.ManyToManyField(Genre)
    season = models.ManyToManyField(Season)
    rating = models.IntegerField()

    def __str__(self):
        return f'{self.anime_id}: {self.anime_name} {self.description} {self.platform} {self.day} {self.time} {self.genre} {self.season} {self.rating}'
    
class WebUser(models.Model):
    fav_anime = models.ManyToManyField(Anime, blank=True, through='Favorite')
    d_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.d_user}: {self.fav_anime}'

class Favorite(models.Model):
    user = models.ForeignKey(WebUser, on_delete=models.CASCADE)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}: {self.anime}'

    class Meta:
        unique_together = [['user', 'anime']]