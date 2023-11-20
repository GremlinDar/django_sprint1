from django.urls import path
from . import views

app_name: str = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<int:id>/', views.post_detail, name='post_detail'),
    path('category/<slug:category_clug>/', views.category_posts, name='category_posts'),
]