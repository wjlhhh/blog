"""定义blogs的URL模式"""
from django.urls import include, path,re_path
from . import views

app_name = 'blogs'
urlpatterns = [
    #主页
    path('', views.index, name='index'),
    re_path('titles/(?P<title_id>\d+)/', views.title, name='title'),
    re_path('new_title/', views.new_title, name='new_title'),
    re_path('edit_title/(?P<title_id>\d+)/', views.edit_title, name='edit_title'),
]