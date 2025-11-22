from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from inventory.models import DonationRequest
from users.models import User

class VolunteerRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.role == User.Role.VOLUNTEER or self.request.user.is_staff

class VolunteerDashboardView(LoginRequiredMixin, VolunteerRequiredMixin, ListView):
    model = DonationRequest
    template_name = 'users/volunteer_dashboard.html'
    context_object_name = 'pending_donations'

    def get_queryset(self):
        return DonationRequest.objects.filter(status=DonationRequest.Status.PENDING).order_by('created_at')

def pre_verify_donation(request, pk):
    if not request.user.is_authenticated or request.user.role != User.Role.VOLUNTEER:
        return redirect('home')
    
    donation = get_object_or_404(DonationRequest, pk=pk)
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'approve':
            donation.status = DonationRequest.Status.APPROVED_TO_SHIP
            donation.admin_notes = f"Pre-verified by Volunteer {request.user.email}"
        elif action == 'reject':
            donation.status = DonationRequest.Status.REJECTED
            donation.admin_notes = f"Rejected by Volunteer {request.user.email}: {request.POST.get('reason')}"
        donation.save()
    return redirect('volunteer_dashboard')
