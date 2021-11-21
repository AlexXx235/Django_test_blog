from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
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


class AddArticleView(LoginRequiredMixin, CreateView):
    form_class = AddArticleForm
    template_name = 'blog/add_article.html'
    login_url = 'blog:home'


class RegisterUserView(CreateView):
    form_class = RegisterUserForm
    template_name = 'blog/register.html'
    success_url = reverse_lazy('blog:home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('blog:home')


class LoginUserView(LoginView):
    form_class = LoginUserForm
    template_name = 'blog/register.html'

    def get_success_url(self):
        return reverse_lazy('blog:home')


def logout_user(request):
    logout(request)
    return redirect('blog:login')


def about(request):
    return render(request, 'blog/about.html')