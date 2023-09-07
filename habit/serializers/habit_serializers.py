from rest_framework.serializers import ModelSerializer
from habit.models import Habit
from habit.validators import HabitValidator


class HabitSerializer(ModelSerializer):
    """Сериализатор для модели Habit, выводит все поля модели, используется валидация"""
    class Meta:
        model = Habit
        fields = '__all__'
        validators = [HabitValidator]
