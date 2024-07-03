from django.db import models
from users.models import CustomUser, Profile
from django.urls import reverse


class Genre(models.Model):
    name = models.CharField('Имя жанра', max_length=50)
    slug = models.SlugField('URL', max_length=50, unique=True)

    # def get_absolute_url(self):
    #     return reverse('genre', kwargs={'genre_slug': self.slug})

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Genre'
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Film(models.Model):

    Y = 'Да'
    N = 'Нет'
    BY_SUBSCRIPTION = (
        (Y, 'Да'),
        (N, 'Нет'),
    )

    U = 'США'
    R = 'Россия'
    UK = 'Великобритания'
    F = 'Франция'
    N = 'Япония'
    COUNTRY = (
        (U, 'США'),
        (R, 'Россия'),
        (UK, 'Великобритания'),
        (F, 'Франция'),
        (N, 'Япония'),
    )

    by_subscription = models.CharField('По подписке', default='Нет', max_length=10, choices=BY_SUBSCRIPTION)
    image = models.ImageField('Изображение', upload_to='images_films/')
    name = models.CharField('Название', max_length=50)
    genre = models.ManyToManyField(Genre)
    # slug = models.SlugField('URL', max_length=50, unique=True)
    text = models.TextField('Описание')
    country = models.CharField('Страна', default='США', max_length=50, choices=COUNTRY)
    director = models.CharField('Режиссёр', max_length=50)

    # def get_absolute_url(self):
    #     return reverse('genre', kwargs={'genre_slug': self.genre.slug})

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Film'
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'


class Comment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    text = models.TextField('Текст')

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = 'comment'
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class RatingMark(models.Model):
    mark = models.SmallIntegerField('Оценка')

    def __str__(self):
        return f'Оценка: {self.mark}'
    
    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'


class Rating(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    mark = models.ForeignKey(RatingMark, on_delete=models.CASCADE)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


# class Person(models.Model):
#     image = models.ImageField('Фото', upload_to='images_persons/')
#     name = models.CharField('Имя', max_length=50)
#     films = models.ManyToManyField(Film)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         db_table = 'Person'
#         verbose_name = 'Персона'
#         verbose_name_plural = 'Персоны'