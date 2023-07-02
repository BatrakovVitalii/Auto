from django.db import models

# Create your models here.
class AutoComponents (models.Model):
    title = models.CharField(
        max_length=128,
        verbose_name='Модель'
    )
    country = models.CharField(
        max_length=128,
        verbose_name='Страна происхождения'
    )
    power = models.CharField(
        max_length=32,
        verbose_name='Мощность'
    )
    drive = models.CharField(
        max_length=32,
        verbose_name='Привод'
    )
    comment = models.TextField(
        verbose_name='Комментарии'
    )


    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'