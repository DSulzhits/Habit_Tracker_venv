from django.db import models
from users.models import User

NULLABLE = {'null': True, 'blank': True}


class Habit(models.Model):
    """Модель полезной привычки, связана внешним ключом с моделью User"""
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='создатель привычки', **NULLABLE)
    name = models.CharField(max_length=150, verbose_name='название')
    place = models.CharField(max_length=150, verbose_name='место')
    time = models.TimeField(verbose_name='время')
    action = models.CharField(max_length=150, verbose_name='выполняемое действие')
    is_pleasant = models.BooleanField(default=True, verbose_name='признак полезной привычки')
    bound_habit = models.ForeignKey('self', on_delete=models.SET_NULL, **NULLABLE, verbose_name='связанная привычка')
    periodic = models.IntegerField(default=1, verbose_name='периодичность дни')
    reward = models.CharField(max_length=150, verbose_name='вознаграждение', **NULLABLE)
    time_for_execution = models.TimeField(verbose_name='время на выполнение', **NULLABLE)
    public = models.BooleanField(default=True, verbose_name='признак публичности')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
