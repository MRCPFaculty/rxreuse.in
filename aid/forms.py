from django import forms
from .models import AidApplication

class AidApplicationForm(forms.ModelForm):
    class Meta:
        model = AidApplication
        fields = ['doctor_prescription', 'income_proof', 'reason_for_aid', 'shipping_address']
        widgets = {
            'shipping_address': forms.Textarea(attrs={'rows': 3}),
        }
