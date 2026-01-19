"""
Django Admin Configuration for Cricket Slot Booking System
"""
from django.contrib import admin
from .models import Slot, Booking


@admin.register(Slot)
class SlotAdmin(admin.ModelAdmin):
    """
    Admin interface for Cricket Slots
    """
    list_display = ('date', 'time_slot', 'cricket_type', 'booked_count', 'max_players', 'is_available')
    list_filter = ('date', 'cricket_type', 'time_slot')
    search_fields = ('date',)
    ordering = ('-date', 'time_slot')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Slot Details', {
            'fields': ('date', 'time_slot', 'cricket_type')
        }),
        ('Capacity', {
            'fields': ('max_players', 'price')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def booked_count(self, obj):
        """Display number of confirmed bookings"""
        count = obj.booked_count
        max_players = obj.max_players
        return f"{count}/{max_players}"
    booked_count.short_description = "Bookings"
    
    def is_available(self, obj):
        """Display availability status with color coding"""
        if obj.is_available:
            return '✅ Available'
        return '❌ Full'
    is_available.short_description = "Status"


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """
    Admin interface for Bookings
    """
    list_display = ('user', 'slot', 'status', 'created_at')
    list_filter = ('status', 'slot__date', 'slot__cricket_type', 'created_at')
    search_fields = ('user__username', 'user__email', 'slot__date')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Booking Information', {
            'fields': ('user', 'slot')
        }),
        ('Status', {
            'fields': ('status',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def get_queryset(self, request):
        """Optimize queryset"""
        qs = super().get_queryset(request)
        return qs.select_related('user', 'slot')
    
    actions = ['mark_confirmed', 'mark_cancelled']
    
    def mark_confirmed(self, request, queryset):
        """Admin action to mark bookings as confirmed"""
        updated = queryset.update(status='confirmed')
        self.message_user(request, f'{updated} booking(s) marked as confirmed.')
    mark_confirmed.short_description = "Mark selected bookings as confirmed"
    
    def mark_cancelled(self, request, queryset):
        """Admin action to mark bookings as cancelled"""
        updated = queryset.update(status='cancelled')
        self.message_user(request, f'{updated} booking(s) marked as cancelled.')
    mark_cancelled.short_description = "Mark selected bookings as cancelled"


# Customize admin site
admin.site.site_header = "🏏 Cricket Booking System Admin"
admin.site.site_title = "Cricket Admin"
admin.site.index_title = "Welcome to Cricket Booking Admin Panel"
