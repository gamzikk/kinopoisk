# Generated by Django 4.2.1 on 2023-06-19 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0005_comment_film_rating'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rating',
            options={'verbose_name': 'Отзыв', 'verbose_name_plural': 'Отзывы'},
        ),
    ]
