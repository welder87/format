from django.contrib import admin

from events.models import EventUser


class EventUserInline(admin.TabularInline):
    model = EventUser
    verbose_name = 'Пользователи'
    verbose_name_plural = 'Пользователи'
    fk_name = 'event'
