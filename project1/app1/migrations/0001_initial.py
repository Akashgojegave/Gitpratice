# Generated by Django 5.0.3 on 2024-03-27 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anime_name', models.CharField(max_length=50)),
                ('anime_year', models.CharField(max_length=50)),
            ],
        ),
    ]
