from rest_framework import serializers
from datetime import time


def HabitValidator(value):
    """Валидаторы, для ограничений параметров создаваемых полезных привычек:
    Исключён одновременный выбор связанной привычки и указания вознаграждения.
    Время выполнения должно быть не больше 120 секунд.
    В связанные привычки могут попадать только привычки с признаком приятной привычки.
    У приятной привычки не может быть вознаграждения или связанной привычки.
    Нельзя выполнять привычку реже, чем 1 раз в 7 дней."""

    if value.get('bound_habit') and value.get('reward'):
        raise serializers.ValidationError('Исключён одновременный выбор связанной привычки и указания вознаграждения.')
    if value.get('time_for_execution') > time(00, 2):
        raise serializers.ValidationError('Время выполнения должно быть не больше 120 секунд.')
    if 'bound_habit' in value and value.get('bound_habit').is_pleasant:
        raise serializers.ValidationError('В связанные привычки могут попадать только привычки с признаком приятной '
                                          'привычки.')
    if value.get('bound_habit') and value.get('reward'):
        raise serializers.ValidationError('У приятной привычки не может быть вознаграждения или связанной привычки.')
    if value.get('periodic') > 7:
        raise serializers.ValidationError('Нельзя выполнять привычку реже, чем 1 раз в 7 дней.')
