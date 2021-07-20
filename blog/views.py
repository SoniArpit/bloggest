from django.db import models
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Post

class Home(ListView):
    model = Post
    template_name = "blog/home.html"
    context_object_name = 'posts'
    ordering = '-pub_date'
    paginate_by = 1

class PostDetail(DetailView):
    model = Post
    