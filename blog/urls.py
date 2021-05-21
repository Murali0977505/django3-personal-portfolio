from django.urls import path
from . import views

app_name='blog'

urlpatterns=[path('', views.all_blogs, name='all_blogs'),
path('test/', views.test, name='test'),
path('<int:blog_id>/', views.detail, name='detail'),]