from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

class DonationRequest(models.Model):
    class Status(models.TextChoices):
        PENDING = 'PENDING', _('Pending Verification')
        APPROVED_TO_SHIP = 'APPROVED_TO_SHIP', _('Approved - Please Ship')
        SHIPPED_BY_DONOR = 'SHIPPED_BY_DONOR', _('Shipped by Donor')
        RECEIVED = 'RECEIVED', _('Received at Warehouse')
        REJECTED = 'REJECTED', _('Rejected')

    donor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='donations')
    medicine_name = models.CharField(max_length=200)
    quantity = models.CharField(max_length=100, help_text="e.g., 2 strips, 1 bottle")
    expiry_date = models.DateField()
    batch_number = models.CharField(max_length=100)
    
    # Proof Images
    image_front = models.ImageField(upload_to='donations/front/')
    image_back = models.ImageField(upload_to='donations/back/')
    image_expiry = models.ImageField(upload_to='donations/expiry/')

    # Logistics
    courier_name = models.CharField(max_length=100, blank=True)
    tracking_id = models.CharField(max_length=100, blank=True)
    
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    admin_notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.medicine_name} - {self.donor.email}"

class InventoryItem(models.Model):
    donation = models.OneToOneField(DonationRequest, on_delete=models.CASCADE, related_name='inventory_item')
    medicine_name = models.CharField(max_length=200)
    batch_number = models.CharField(max_length=100)
    expiry_date = models.DateField()
    is_allocated = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.medicine_name
