from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import DonationRequest
from .forms import DonationForm, TrackingForm

class DonateMedicineView(LoginRequiredMixin, CreateView):
    model = DonationRequest
    form_class = DonationForm
    template_name = 'inventory/donation_form.html'
    success_url = reverse_lazy('my_donations')

    def form_valid(self, form):
        form.instance.donor = self.request.user
        return super().form_valid(form)

class DonationListView(LoginRequiredMixin, ListView):
    model = DonationRequest
    template_name = 'inventory/donation_list.html'
    context_object_name = 'donations'

    def get_queryset(self):
        return DonationRequest.objects.filter(donor=self.request.user).order_by('-created_at')

class AddTrackingView(LoginRequiredMixin, UpdateView):
    model = DonationRequest
    form_class = TrackingForm
    template_name = 'inventory/tracking_form.html'
    success_url = reverse_lazy('my_donations')

    def get_queryset(self):
        # Only allow editing if status is APPROVED_TO_SHIP
        return super().get_queryset().filter(donor=self.request.user, status=DonationRequest.Status.APPROVED_TO_SHIP)

    def form_valid(self, form):
        form.instance.status = DonationRequest.Status.SHIPPED_BY_DONOR
        return super().form_valid(form)
