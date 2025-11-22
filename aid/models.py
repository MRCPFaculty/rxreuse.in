from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from inventory.models import InventoryItem

class AidApplication(models.Model):
    class Status(models.TextChoices):
        PENDING = 'PENDING', _('Pending Verification')
        APPROVED = 'APPROVED', _('Approved - Pay Shipping')
        PAID = 'PAID', _('Shipping Paid')
        DISPATCHED = 'DISPATCHED', _('Dispatched')
        DELIVERED = 'DELIVERED', _('Delivered')
        REJECTED = 'REJECTED', _('Rejected')

    beneficiary = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='aid_applications')
    requested_medicines = models.ManyToManyField(InventoryItem, blank=True) # Specific items allocated by Admin later
    
    # Requirements
    doctor_prescription = models.ImageField(upload_to='aid/prescriptions/')
    income_proof = models.ImageField(upload_to='aid/income_proof/')
    reason_for_aid = models.TextField()

    # Logistics
    shipping_address = models.TextField()
    shipping_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    razorpay_order_id = models.CharField(max_length=100, blank=True)
    razorpay_payment_id = models.CharField(max_length=100, blank=True)
    shiprocket_order_id = models.CharField(max_length=100, blank=True)
    tracking_link = models.URLField(blank=True)

    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    admin_notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Aid App #{self.id} - {self.beneficiary.email}"
