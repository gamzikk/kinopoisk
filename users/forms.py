from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError

from .models import CustomUser, UserSubscription, Subscription


class RegisterForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Enter password'}), min_length=6)
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Repeat password'}))

	class Meta:
		model = CustomUser
		exclude = ['is_staff']
		widgets = {
			'username': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Enter username'}),
			'email': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Enter email'}),
			'phone': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Enter phone'}),
		}

	def clean_password2(self):
		cd = self.cleaned_data
		if cd['password'] != cd ['password2']:
			raise forms.ValidationError('Password don\'t match')
		return cd['password2']


class LoginForm(forms.Form):
	email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Enter email'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Enter password'}))


class SubscribeForm(forms.ModelForm):
	subscription = forms.ModelChoiceField(queryset=Subscription.objects.all())

	class Meta:
		model = UserSubscription
		fields = ['subscription']


class ContactForm(forms.Form):
	from_email = forms.EmailField()
	subject = forms.CharField()
	message = forms.CharField()