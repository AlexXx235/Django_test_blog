from django.urls import path
from . import views


app_name = 'blog'
urlpatterns = [
    path('', views.index, name='home'),
    path('articles/', views.articles, name='articles'),
    path('login/', views.login, name='login'),
    path('add_article/', views.add_article, name='add_article'),
    path('about/', views.about, name='about'),
    path('articles/<int:article_id>/', views.article, name='article'),
]