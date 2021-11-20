from django import forms
from .models import *


class AddArticleForm(forms.Form):
    title = forms.CharField(max_length=256, label='Заголовок',
                            widget=forms.TextInput(attrs={'class': 'add-article-form__input'}))
    text = forms.CharField(widget=forms.Textarea(attrs={
        'cols': 60,
        'rows': 10,
        'class': 'add-article-form__input'}),
        label='Текст')
