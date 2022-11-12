# Generated by Django 4.1.1 on 2022-11-12 09:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sekujuru_app', '0004_remove_webuser_d_user_remove_webuser_fav_anime_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sekujuru_app.anime')),
            ],
        ),
        migrations.CreateModel(
            name='WebUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('fav_anime', models.ManyToManyField(blank=True, through='user.Favorite', to='sekujuru_app.anime')),
            ],
        ),
        migrations.AddField(
            model_name='favorite',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.webuser'),
        ),
        migrations.AlterUniqueTogether(
            name='favorite',
            unique_together={('user', 'anime')},
        ),
    ]