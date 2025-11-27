from django.contrib import admin
from .models import UserBadge, PlatformStats, MonetaryDonation, ContactMessage
from .success_models import SuccessStory
from .contact_admin import ContactMessageAdmin

admin.site.register(UserBadge)
admin.site.register(PlatformStats)
admin.site.register(MonetaryDonation)
admin.site.register(SuccessStory)
