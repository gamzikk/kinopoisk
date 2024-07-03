from django.urls import path
from django.views.decorators.cache import cache_page

from . import views

urlpatterns = [
    path('', views.getFilms.as_view(), name='films'),
    # path('<int:film_id>/', views.getFilm.as_view(), name='film'),
    path('<int:film_id>/', views.film, name='film'),
    path('genre/<slug:slug>/', views.getGenre.as_view(), name='genre'),

    # path('', views.getFilms, name='films'),
    # path('<int:film_id>/', views.getFilm, name='film'),
    # path('comedy/', views.getComedys),
    # path('comedy/', views.getComedys.as_view()),
    # path('cartoon/', views.getCartoons),
    # path('thriller/', views.getThrillers),
    # path('fantasy/', views.getFantasys),
    # path('drama/', views.getDramas),
    # path('', views.test),
    # path('test/', views.test),
]
