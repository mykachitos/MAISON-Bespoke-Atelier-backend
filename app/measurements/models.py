from django.db import models


class MeasurementRequest(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новая'),
        ('contacted', 'Связались'),
        ('scheduled', 'Записана'),
        ('done', 'Завершена'),
    ]

    full_name = models.CharField(max_length=120, verbose_name='Имя')
    phone = models.CharField(max_length=30, verbose_name='Телефон')
    email = models.EmailField(blank=True, verbose_name='Email')
    preferred_time = models.CharField(max_length=120, blank=True, verbose_name='Удобное время')
    wishes = models.TextField(blank=True, verbose_name='Пожелания')
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='new',
        verbose_name='Статус',
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'заявка на мерки'
        verbose_name_plural = 'заявки на мерки'

    def __str__(self):
        return f'{self.full_name} ({self.phone})'

