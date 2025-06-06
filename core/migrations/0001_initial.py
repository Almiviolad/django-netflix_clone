# Generated by Django 5.2 on 2025-05-10 14:07

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tmdb_id', models.IntegerField(unique=True)),
                ('genre_name', models.CharField(verbose_name=50)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('movie_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('release_date', models.DateField()),
                ('overview', models.TextField(max_length=700)),
                ('poster', models.ImageField(upload_to='movie_images/')),
                ('popularity', models.DecimalField(decimal_places=3, max_digits=6)),
                ('genres', models.ManyToManyField(to='core.genre')),
            ],
        ),
    ]
