from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import UserManager

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = 'ADMIN', _('Admin')
        VOLUNTEER = 'VOLUNTEER', _('Volunteer')
        DONOR = 'DONOR', _('Donor')
        BENEFICIARY = 'BENEFICIARY', _('Beneficiary')

    username = None
    email = models.EmailField(_('email address'), unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    is_phone_verified = models.BooleanField(default=False)
    role = models.CharField(max_length=20, choices=Role.choices, default=Role.DONOR)

    # Address Fields
    address_line1 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100, blank=True)
    pincode = models.CharField(max_length=10, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email
