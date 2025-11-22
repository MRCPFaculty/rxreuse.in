from django.contrib import admin
from .models import AidApplication

@admin.register(AidApplication)
class AidApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'beneficiary', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('beneficiary__email', 'razorpay_payment_id')
    readonly_fields = ('created_at', 'updated_at')
