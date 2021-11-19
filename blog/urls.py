from django.urls import path
from . import views


app_name = 'blog'
urlpatterns = [
    path('', views.index, name='home'),
    path('articles/', views.articles, name='articles'),
    path('login/', views.login, name='login')
]