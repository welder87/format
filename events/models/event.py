from django.contrib.auth import get_user_model
from django.db import models


class Event(models.Model):
    name = models.CharField(
        verbose_name='Событие',
        max_length=254,
    )
    start_date = models.DateField()
    users = models.ManyToManyField(
        to=get_user_model(),
        through='EventUser',
        through_fields=(
            'event',
            'user',
        ),
        verbose_name='Пользователи',
        related_name='events',
    )

    class Meta:
        ordering = [
            'id',
        ]
        verbose_name = 'Событие'
        verbose_name_plural = 'События'
