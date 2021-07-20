
from django.urls import path
from django.contrib import admin
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('<int:pk>/', views.PostDetail.as_view(), name="post_detail"),
    path('create-post/', views.PostCreate.as_view(), name="post_create"),
]