from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import AidApplication
from .forms import AidApplicationForm
from inventory.models import InventoryItem

class AvailableMedicinesView(ListView):
    model = InventoryItem
    template_name = 'aid/available_medicines.html'
    context_object_name = 'medicines'

    def get_queryset(self):
        # Show only items that are RECEIVED (in stock) and NOT ALLOCATED
        # Assuming InventoryItem is created only when Donation is RECEIVED
        return InventoryItem.objects.filter(is_allocated=False)

class ApplyForAidView(LoginRequiredMixin, CreateView):
    model = AidApplication
    form_class = AidApplicationForm
    template_name = 'aid/aid_form.html'
    success_url = reverse_lazy('aid_dashboard')

    def form_valid(self, form):
        form.instance.beneficiary = self.request.user
        return super().form_valid(form)

class AidDashboardView(LoginRequiredMixin, ListView):
    model = AidApplication
    template_name = 'aid/aid_dashboard.html'
    context_object_name = 'applications'

    def get_queryset(self):
        return AidApplication.objects.filter(beneficiary=self.request.user).order_by('-created_at')
