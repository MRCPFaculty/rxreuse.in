from django.views.generic import ListView
from .models import Badge

class SuccessStoriesView(ListView):
    model = Badge  # Placeholder - using Badge model for now
    template_name = 'community/success_stories.html'
    context_object_name = 'stories'
    
    def get_queryset(self):
        # Return empty queryset for now since we don't have a SuccessStory model yet
        return Badge.objects.none()
