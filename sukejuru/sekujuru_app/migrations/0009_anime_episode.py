# Generated by Django 4.1.2 on 2022-11-19 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sekujuru_app", "0008_anime_rating"),
    ]

    operations = [
        migrations.AddField(
            model_name="anime",
            name="episode",
            field=models.ManyToManyField(to="sekujuru_app.episode"),
        ),
    ]
