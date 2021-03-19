from django.contrib import admin

from events.models import Event
from .event_user import EventUserInline


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'start_date',
    ]
    search_fields = [
        'name',
    ]
    inlines = [
        EventUserInline,
    ]
