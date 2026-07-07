from django.db import models
from django.core.validators import RegexValidator

class SiteSettings(models.Model):
    primary_color = models.CharField(
        max_length=7,
        default='#0d6efd',
        validators=[RegexValidator(r'^#[0-9a-fA-F]{6}$', 'Введите корректный HEX-цвет')],
        verbose_name='Основной цвет кнопок'
    )
    # при необходимости добавьте другие настройки

    class Meta:
        verbose_name = 'Настройки сайта'
        verbose_name_plural = 'Настройки сайта'

    def __str__(self):
        return 'Текущие настройки'

    @classmethod
    def get_solo(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj