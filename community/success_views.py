from django.views.generic import ListView
from .success_models import SuccessStory

class SuccessStoriesView(ListView):
    model = SuccessStory
    template_name = 'community/success_stories.html'
    context_object_name = 'stories'
    ordering = ['-created_at']
