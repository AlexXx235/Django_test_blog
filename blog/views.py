from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from .models import *
from .forms import *

# Create your views here.
header_menu = [
    {'title': 'Главная', 'url_name': 'blog:home'},
    {'title': 'Статьи', 'url_name': 'blog:articles'},
    {'title': 'Добавить статью', 'url_name': 'blog:add_article'},
    {'title': 'О нас', 'url_name': 'blog:about'}
]


def index(request):
    return render(request, 'blog/home.html')


class ArticlesView(ListView):
    model = Article
    template_name = 'blog/articles.html'
    context_object_name = 'articles'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/article.html'
    context_object_name = 'article'
    pk_url_kwarg = 'article_id'


def login(request):
    return render(request, 'blog/login.html')


class AddArticleView(CreateView):
    form_class = AddArticleForm
    template_name = 'blog/add_article.html'


# def add_article(request):
#     if request.method == 'POST':
#         form = AddArticleForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('blog:articles')
#     else:
#         form = AddArticleForm()
#         print(form)
#     return render(request, 'blog/add_article.html', {'form': form})


def about(request):
    return render(request, 'blog/about.html')