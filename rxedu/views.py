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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get 5 latest posts for sidebar, excluding current post
        context['latest_posts'] = BlogPost.objects.filter(
            is_published=True
        ).exclude(
            pk=self.object.pk
        ).order_by('-published_date')[:5]
        return context
