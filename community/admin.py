from django.contrib import admin
from .models import Badge, UserBadge, PlatformStats, MonetaryDonation

admin.site.register(Badge)
admin.site.register(UserBadge)
admin.site.register(PlatformStats)
admin.site.register(MonetaryDonation)
