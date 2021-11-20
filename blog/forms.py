from django import forms
from django.core.exceptions import ValidationError
from .models import *


class AddArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'text']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'add-article-form__input'}),
            'text': forms.Textarea(attrs={'rows': 10, 'class': 'add-article-form__input'})
        }
