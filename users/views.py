import datetime
from django.shortcuts import render, redirect
from django.conf import settings
from kinopoisk.settings import RECIPIENTS_EMAIL, DEFAULT_FROM_EMAIL
from django.http import HttpResponseRedirect, HttpResponse
from django.dispatch import receiver
from .forms import RegisterForm, LoginForm, SubscribeForm, ContactForm
from django.urls import reverse_lazy, reverse
from django.db.models.signals import post_save
from django.core.mail import send_mail, BadHeaderError

from django.views.generic import CreateView, DetailView

from django.contrib.auth.views import LogoutView
from .models import CustomUser, Profile, UserSubscription
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def register(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			new_user = form.save(commit=False)
			new_user.set_password(form.cleaned_data['password'])
			new_user.save()
			login(request, new_user)
			return redirect('profile', new_user.id)
	else:
		form = RegisterForm()
	return render(request, 'users/register.html', {'form': form})


# class register(CreateView):
# 	form_class = RegisterForm
# 	template_name = 'users/register.html'

# 	def get_success_url(self):
# 		return reverse('profile')


def user_login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			user = authenticate(email=cd['email'], password=cd['password'])
			if user is not None:
				if user.is_active:
					login(request, user)
					return redirect('profile', user.id)
				else:
					return HttpResponse('Отключённая учётная запись')
			else:
				return HttpResponse('Неверный логин или пароль.')
	else:
		form = LoginForm()
	return render(request, 'users/login.html', {'form': form})


def user_logout(request):
	logout(request)
	return redirect('main')


class ProfileView(DetailView):
	model = Profile
	template_name = 'users/profile.html'
	context_object_name = 'profile'

# Альтернатива контроллера profile
# @login_required
# def profile(request, pk):
# 	profile = Profile.objects.get(pk=pk)
# 	return render(request, 'users/profile.html', {'profile': profile})


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_profile(sender, instance, **kwargs):
	instance.profile.save()


def subscribe(request):
	if request.method == "POST":
		form = SubscribeForm(request.POST)
		if form.is_valid():
			form = form.save(commit=False)
			form.user = request.user
			form.save()
			return redirect('main')
	else:
		form = SubscribeForm()
	return render(request, 'users/subscribe.html', {'form': form})


def test(request):
	# sub = UserSubscription.objects.values('subscription')
	# sub = UserSubscription.objects.filter(subscription__name='"Кино Плюс"')
	# sub = UserSubscription.objects.all()
	sub = UserSubscription.objects.prefetch_related().all()
	return render(request, 'users/test.html', {'sub': sub})


def contact(request):
	if request.method == 'GET':
		form = ContactForm()
	elif request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = form.cleaned_data['subject']
			from_email = form.cleaned_data['from_email']
			message = form.cleaned_data['message']
			try:
				send_mail(f'{subject} от {from_email}', message, DEFAULT_FROM_EMAIL, RECIPIENTS_EMAIL)
			except BadHeaderError:
				return HttpResponse('Ошибка в теме письма.')
			return redirect('success')
	else:
		return HttpResponse('Неверный запрос.')
	return render(request, 'users/email.html', {'form': form})

def success(request):
	return HttpResponse('Приняли! Спасибо за вашу заявку.')