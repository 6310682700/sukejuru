# Generated by Django 4.1 on 2022-11-18 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sekujuru_app', '0006_anime_anime_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anime',
            name='rating',
        ),
        migrations.AlterField(
            model_name='anime',
            name='anime_image',
            field=models.CharField(default='https://upload.wikimedia.org/wikipedia/commons/thumb/d/d1/Image_not_available.png/640px-Image_not_available.png', max_length=999),
        ),
    ]
