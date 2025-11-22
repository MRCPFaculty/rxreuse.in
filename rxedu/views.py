from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import BlogPost

class BlogListView(ListView):
    model = BlogPost
    template_name = 'rxedu/blog_list.html'
    context_object_name = 'posts'
    queryset = BlogPost.objects.filter(is_published=True).order_by('-published_date')

class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'rxedu/blog_detail.html'
    context_object_name = 'post'
