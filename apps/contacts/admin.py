from django.contrib import admin
from .models import Contact, Newsletter

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['parent_name', 'phone', 'email', 'child_age', 'is_contacted', 'created_at']
    list_filter = ['is_contacted', 'created_at', 'child_age']
    search_fields = ['parent_name', 'phone', 'email']
    list_editable = ['is_contacted']
    readonly_fields = ['created_at']
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('Thông tin phụ huynh', {
            'fields': ('parent_name', 'phone', 'email')
        }),
        ('Thông tin trẻ', {
            'fields': ('child_age', 'message')
        }),
        ('Trạng thái', {
            'fields': ('is_contacted', 'created_at')
        }),
    )

@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ['email', 'subscribed_at', 'is_active']
    list_filter = ['is_active', 'subscribed_at']
    search_fields = ['email']
    list_editable = ['is_active']
    readonly_fields = ['subscribed_at']
    date_hierarchy = 'subscribed_at'