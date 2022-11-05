# Generated by Django 4.1.1 on 2022-11-05 14:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('anime_id', models.IntegerField(primary_key=True, serialize=False)),
                ('anime_name', models.CharField(max_length=99)),
                ('description', models.CharField(max_length=999)),
                ('time', models.TimeField()),
                ('rating', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='AnimePlatforms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=99)),
            ],
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=99)),
            ],
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sekujuru_app.anime')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=99)),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season', models.CharField(max_length=99)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('fav_anime', models.ManyToManyField(blank=True, through='sekujuru_app.Favorite', to='sekujuru_app.anime')),
            ],
        ),
        migrations.AddField(
            model_name='favorite',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sekujuru_app.users'),
        ),
        migrations.AddField(
            model_name='anime',
            name='anime_genre',
            field=models.ManyToManyField(to='sekujuru_app.genre'),
        ),
        migrations.AddField(
            model_name='anime',
            name='anime_season',
            field=models.ManyToManyField(to='sekujuru_app.season'),
        ),
        migrations.AddField(
            model_name='anime',
            name='day',
            field=models.ManyToManyField(to='sekujuru_app.day'),
        ),
        migrations.AddField(
            model_name='anime',
            name='platform',
            field=models.ManyToManyField(to='sekujuru_app.animeplatforms'),
        ),
        migrations.AlterUniqueTogether(
            name='favorite',
            unique_together={('user', 'anime')},
        ),
    ]