from django.urls import path
from . import views

urlpatterns = [
    path('api', views.index, name='index'),
    path('', views.all_posts, name='get_posts'),
    path('new_post', views.new_post, name='create_post'),
    path('new_category', views.new_category, name='create_category')
]