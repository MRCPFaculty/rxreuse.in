from django import forms
from .models import DonationRequest

class DonationForm(forms.ModelForm):
    class Meta:
        model = DonationRequest
        fields = ['medicine_name', 'quantity', 'expiry_date', 'batch_number', 'image_front', 'image_back', 'image_expiry']
        widgets = {
            'expiry_date': forms.DateInput(attrs={'type': 'date'}),
        }

class TrackingForm(forms.ModelForm):
    class Meta:
        model = DonationRequest
        fields = ['courier_name', 'tracking_id']
