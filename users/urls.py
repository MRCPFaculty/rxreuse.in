from django.urls import path
from .volunteer_views import VolunteerDashboardView, pre_verify_donation

urlpatterns = [
    path('volunteer/dashboard/', VolunteerDashboardView.as_view(), name='volunteer_dashboard'),
    path('volunteer/verify/<int:pk>/', pre_verify_donation, name='pre_verify_donation'),
]
