from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'blog/home.html')


def articles(request):
    return render(request, 'blog/articles.html')


def login(request):
    return render(request, 'blog/login.html')