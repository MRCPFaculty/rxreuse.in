from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.contrib import messages
from .contact_forms import ContactForm

class ContactView(FormView):
    template_name = 'pages/contact.html'
    form_class = ContactForm
    success_url = '/contact/'
    
    def form_valid(self, form):
        form.save()
        messages.success(self.request, '✅ Thank you! Your message has been sent successfully. We\'ll get back to you soon.')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, '❌ Oops! There was an error sending your message. Please check the form and try again.')
        return super().form_invalid(form)
