from django.urls import path
from . import views

urlpatterns = [
	path('register/', views.register, name='register'),
	path('login/', views.user_login, name='login'),
	path('logout/', views.user_logout, name='logout'),
	path('profile/<int:pk>/', views.ProfileView.as_view(), name='profile'),
	path('subscribe', views.subscribe, name='subscribe'),
	path('contact/', views.contact, name='contact'),
	path('succes/', views.success, name='success'),
	path('test/', views.test),
]