from django import forms
from .contact_models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Your Name',
                'style': 'background: rgba(0,0,0,0.2); border-color: rgba(255,255,255,0.1); color: white;'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'your@email.com',
                'style': 'background: rgba(0,0,0,0.2); border-color: rgba(255,255,255,0.1); color: white;'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'How can we help?',
                'style': 'background: rgba(0,0,0,0.2); border-color: rgba(255,255,255,0.1); color: white;'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 6,
                'placeholder': 'Tell us more about your inquiry...',
                'style': 'background: rgba(0,0,0,0.2); border-color: rgba(255,255,255,0.1); color: white;'
            }),
        }
