from django.contrib import admin
from voices.models import RecordHistory


@admin.register(RecordHistory)
class RecordHistoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'record', 'created_at']
    list_display_links = ['id', 'user', 'record']
