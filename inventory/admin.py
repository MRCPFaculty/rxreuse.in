from django.contrib import admin
from .models import DonationRequest, InventoryItem

@admin.register(DonationRequest)
class DonationRequestAdmin(admin.ModelAdmin):
    list_display = ('medicine_name', 'donor', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('medicine_name', 'donor__email')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(InventoryItem)
class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ('medicine_name', 'expiry_date', 'is_allocated')
    list_filter = ('is_allocated',)
