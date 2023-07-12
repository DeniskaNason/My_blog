from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView
from .models import Post


class Index(ListView):
    template_name = 'blog/index.html'
    model = Post
    context_object_name = 'posts'


class Post(DetailView):
    template_name = 'blog/post.html'
    model = Post
    context_object_name = 'post'

# def post(request):
#     return render(request, 'blog/post.html')

# class Offer(DetailView):
#     template_name = ''
#     model =
#     context_object_name = 'tags'
#     pass
