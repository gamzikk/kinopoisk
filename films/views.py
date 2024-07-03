import datetime
# from querybuilder.query import Query
from django.db import connection
from collections import namedtuple

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Film, Genre, Comment
from users.models import UserSubscription, Subscription

from .forms import CommentForm, RatingForm


class getFilms(ListView):
    model = Film
    template_name = 'films/films.html'
    context_object_name = 'films'


# class getFilm(DetailView):
#     model = Film
#     template_name = 'films/film.html'
#     context_object_name = 'film'
#     pk_url_kwarg = 'film_id'


def film(request, film_id):
    film = Film.objects.get(pk=film_id)
    subscription = Subscription.objects.get(name='"Кино Плюс"')
    comments = Comment.objects.filter(film=film)

    if request.user.is_authenticated:
        try:
            sub = UserSubscription.objects.get(user=request.user)
        except UserSubscription.DoesNotExist:
            sub = None
    else:
        sub = None

    if film.by_subscription == 'Да':
        if sub is None:
            if request.method == 'POST':
                form = RatingForm(request.POST)
                if form.is_valid():
                    form = form.save(commit=False)
                    form.user = request.user
                    form.film = film
                    form.save()
            else:
                form = RatingForm()
            if request.method == 'POST':
                comment_form = CommentForm(request.POST)
                if comment_form.is_valid():
                    comment = comment_form.save(commit=False)
                    comment.user = request.user
                    comment.film = film
                    comment.save()
            else:
                comment_form = CommentForm()
            return render(request, 'films/pay_film.html', {'film': film, 'form': form, 'comment_form': comment_form, 'comments': comments})
        elif sub is not None:
            date_now = datetime.date.today()
            year = sub.date.year
            month = sub.date.month
            day = sub.date.day
            date = datetime.date(year, month, day)
            check = (date_now - date).days
            if check <= subscription.time_limit:
                if request.method == 'POST':
                    form= RatingForm(request.POST)
                    if form.is_valid():
                        form = form.save(commit=False)
                        form.user = request.user
                        form.film = film
                        form.save()
                else:
                    form = RatingForm()
                if request.method == 'POST':
                    comment_form = CommentForm(request.POST)
                    if comment_form.is_valid():
                        comment = comment_form.save(commit=False)
                        comment.user = request.user
                        comment.film = film
                        comment.save()
                else:
                    comment_form = CommentForm()
                return render(request, 'films/film.html', {'film': film, 'form': form, 'comment_form': comment_form, 'comments': comments})
            else:
                if request.method == 'POST':
                    form= RatingForm(request.POST)
                    if form.is_valid():
                        form = form.save(commit=False)
                        form.user = request.user
                        form.film = film
                        form.save()
                else:
                    form = RatingForm()
                if request.method == 'POST':
                    comment_form = CommentForm(request.POST)
                    if comment_form.is_valid():
                        comment = comment_form.save(commit=False)
                        comment.user = request.user
                        comment.film = film
                        comment.save()
                else:
                    comment_form = CommentForm()
                return render(request, 'films/pay_film.html', {'film': film, 'form': form, 'comment_form': comment_form, 'comments': comments})
    else:
        if request.method == 'POST':
            form= RatingForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                form.user = request.user
                form.film = film
                form.save()
        else:
            form = RatingForm()
        if request.method == 'POST':
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.user = request.user
                comment.film = film
                comment.save()
        else:
            comment_form = CommentForm()
        return render(request, 'films/film.html', {'film': film, 'form': form, 'comment_form': comment_form, 'comments': comments})


class getGenre(ListView):
    model = Film
    template_name = 'films/genres.html'
    context_object_name = 'films'

    def get_queryset(self):
        return Film.objects.filter(genre__slug=self.kwargs['slug'])