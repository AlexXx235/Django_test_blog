from django.urls import path
from . import views


app_name = 'blog'
urlpatterns = [
    path('', views.index, name='home'),
    path('articles/<int:article_id>/', views.ArticleDetailView.as_view(), name='article'),
    path('articles/', views.ArticlesView.as_view(), name='articles'),
    path('login/', views.LoginUserView.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.RegisterUserView.as_view(), name='register'),
    path('add_article/', views.AddArticleView.as_view(), name='add_article'),
    path('about/', views.about, name='about'),
]