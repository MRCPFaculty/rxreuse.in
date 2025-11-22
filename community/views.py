from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import PlatformStats, UserBadge, MonetaryDonation
from inventory.models import DonationRequest

class ImpactDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'community/impact_dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['my_donations_count'] = DonationRequest.objects.filter(donor=user).count()
        context['my_badges'] = UserBadge.objects.filter(user=user)
        # Mock calculation for lives impacted
        context['lives_impacted'] = context['my_donations_count'] * 2 
        return context

class TransparencyHubView(TemplateView):
    template_name = 'community/transparency_hub.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        stats = PlatformStats.objects.first()
        if not stats:
            stats = PlatformStats.objects.create()
        context['stats'] = stats
        context['recent_donors'] = MonetaryDonation.objects.filter(is_successful=True).order_by('-created_at')[:5]
        return context
