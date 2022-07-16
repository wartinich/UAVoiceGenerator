from django.contrib import admin
from apps.voices.models import Record, RecordHistory


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ['id', 'record_text']
    list_display_links = ['id', 'record_text']


@admin.register(RecordHistory)
class RecordHistoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'record', 'created_at']
    list_display_links = ['id', 'user', 'record']
