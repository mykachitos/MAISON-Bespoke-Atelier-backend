from django.contrib import admin

from .models import MeasurementRequest


@admin.register(MeasurementRequest)
class MeasurementRequestAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'preferred_time', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('full_name', 'phone', 'email', 'wishes')
    readonly_fields = ('created_at',)

