from django.db import models
from django.conf import settings
from .success_models import SuccessStory

class Badge(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.ImageField(upload_to='badges/')
    criteria = models.CharField(max_length=200, help_text="e.g., '5_donations'")

    def __str__(self):
        return self.name

class UserBadge(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='badges')
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE)
    earned_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'badge')

class PlatformStats(models.Model):
    total_donations = models.IntegerField(default=0)
    lives_impacted = models.IntegerField(default=0)
    medicines_distributed = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Stats as of {self.updated_at}"

class MonetaryDonation(models.Model):
    donor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    email = models.EmailField(blank=True) # For guest donors
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    razorpay_payment_id = models.CharField(max_length=100)
    is_successful = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"₹{self.amount} by {self.email or self.donor}"
