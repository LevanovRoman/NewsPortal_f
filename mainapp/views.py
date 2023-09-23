from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView

from .models import *


menu = [
    {'title': 'Главная', 'url_name': 'main'},
    {'title': 'Все новости', 'url_name': 'show_all_posts'},
    # {'title': 'Обо мне', 'url_name': 'post'},
    # {'title': 'Портфолио', 'url_name': 'category'},
]


class MainPage(ListView):
    model = Post
    template_name = 'mainapp/base.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Главная'
        return context


class ShowAllPosts(ListView):
    model = Post
    template_name = 'mainapp/show-all-posts.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Новости'
        return context

    def get_queryset(self):
        return Post.objects.order_by('-time_created')


class ShowPost(DetailView):
    model = Post
    template_name = 'mainapp/post-page.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Новость'
        return context

    def get_success_url(self, **kwargs):
        return reverse_lazy('post', kwargs={'post_slug': self.get_object().slug})

class Category(ListView):
    model = Category
    template_name = 'mainapp/post-page.html'





