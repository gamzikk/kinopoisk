from django import forms
from django.forms import ModelForm

from .models import RatingMark, Rating, Comment


class CommentForm(forms.ModelForm):
    text = forms.CharField()

    class Meta:
        model = Comment
        fields = ['text']


class RatingForm(forms.ModelForm):
    mark = forms.ModelChoiceField(queryset=RatingMark.objects.all())

    class Meta:
        model = Rating
        fields = ['mark']