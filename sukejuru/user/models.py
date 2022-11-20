from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from sekujuru_app.models import Anime

# สร้าง WebUser object เมื่อมีการ create user
@receiver(post_save, sender=User)
def create_user_picks(sender, instance, created, **kwargs):
    if created:
        WebUser.objects.create(d_user=instance)

# Create your models here.
class WebUser(models.Model):
    fav_anime = models.ManyToManyField(Anime, blank=True)
    d_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.d_user}: {self.fav_anime}'