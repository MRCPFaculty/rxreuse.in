from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .contact_forms import ContactForm

class ContactView(FormView):
    template_name = 'pages/contact.html'
    form_class = ContactForm
    success_url = '/contact/'
    
    def form_valid(self, form):
        # Save the form
        contact_message = form.save()
        
        # Send email notification to admin
        subject = f'New Contact Form Submission: {contact_message.subject}'
        message = f"""
New contact form submission received!

From: {contact_message.name}
Email: {contact_message.email}
Subject: {contact_message.subject}

Message:
{contact_message.message}

---
Submitted at: {contact_message.created_at.strftime('%Y-%m-%d %H:%M:%S')}
"""
        
        try:
            send_mail(
                subject=subject,
                message=message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.ADMIN_EMAIL],
                fail_silently=False,
            )
        except Exception as e:
            # Log error but don't fail the form submission
            print(f"Error sending email: {e}")
        
        messages.success(self.request, '✅ Thank you! Your message has been sent successfully. We\'ll get back to you soon.')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, '❌ Oops! There was an error sending your message. Please check the form and try again.')
        return super().form_invalid(form)
