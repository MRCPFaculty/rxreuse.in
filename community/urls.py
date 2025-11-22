from django.urls import path
from .views import ImpactDashboardView, TransparencyHubView
from .success_views import SuccessStoriesView

urlpatterns = [
    path('impact/', ImpactDashboardView.as_view(), name='impact_dashboard'),
    path('transparency/', TransparencyHubView.as_view(), name='transparency_hub'),
    path('stories/', SuccessStoriesView.as_view(), name='success_stories'),
]
