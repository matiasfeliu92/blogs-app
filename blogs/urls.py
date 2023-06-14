from django.urls import path
from . import views

urlpatterns = [
    path('api', views.index, name='index'),
    path('', views.filter_posts, name='get_posts'),
    path('new_post', views.new_post, name='create_post'),
]