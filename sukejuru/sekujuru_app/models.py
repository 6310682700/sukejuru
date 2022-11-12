from django.db import models

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