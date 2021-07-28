
from django.urls import path
from django.contrib import admin
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('<int:pk>/', views.PostDetail.as_view(), name="post_detail"),
    path('create-post/', views.PostCreate.as_view(), name="post_create"),
    path('dashboard/', views.Dashboard.as_view(), name="dashboard"),
    path('<int:pk>/edit/', views.PostUpdate.as_view(), name="post_update"),
    path('<int:pk>/delete/', views.PostDelete.as_view(), name="post_delete"),

]