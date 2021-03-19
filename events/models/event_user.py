from django.contrib.auth import get_user_model
from django.db import models


class EventUser(models.Model):
    event = models.ForeignKey(
        to='Event',
        on_delete=models.CASCADE,
        verbose_name='Событие',
    )
    user = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
    )

    class Meta:
        ordering = [
            'id',
        ]
        constraints = [
            models.UniqueConstraint(
                fields=(
                    'event',
                    'user',
                ),
                name='unique_event_user',
            ),
        ]
        verbose_name = 'Событие - Пользователь'
        verbose_name_plural = 'События - Пользователи'
