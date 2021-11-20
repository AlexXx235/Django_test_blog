from django import forms
from .models import *


class AddArticleForm(forms.Form):
    title = forms.CharField(max_length=256, label='Заголовок')
    text = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label='Текст')
