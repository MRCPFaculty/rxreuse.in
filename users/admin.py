from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'role', 'phone_number', 'is_phone_verified', 'is_staff')
    list_filter = ('role', 'is_staff', 'is_superuser', 'is_phone_verified')
    search_fields = ('email', 'phone_number')
    ordering = ('email',)
