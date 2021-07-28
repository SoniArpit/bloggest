from django.db import models
from django.http import request
from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.base import View
from .models import Post
from django.urls import reverse_lazy

class Home(ListView):
    model = Post
    template_name = "blog/home.html"
    context_object_name = 'posts'
    ordering = '-pub_date'
    paginate_by = 1

class Dashboard(View):
    def get(self, reqeust, *args,**kwargs):
        view = Home.as_view(
            template_name = "blog/admin_page.html",
            paginate_by = 3
        )
        return view(reqeust, *args, **kwargs)

class PostDetail(DetailView):
    model = Post
    def get_object(self):
        object = super(PostDetail, self).get_object()
        object.view_count+=1
        object.save()
        return object

class PostCreate(CreateView):
    model = Post
    fields = ("title", "content", "category")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PostCreate, self).form_valid(form)

class PostUpdate(UpdateView):
    model = Post
    fields = ('title', 'content', 'category')

class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('dashboard')