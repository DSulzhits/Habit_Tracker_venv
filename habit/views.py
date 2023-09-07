from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from habit.models import Habit
from habit.serializers.habit_serializers import HabitSerializer
from rest_framework.permissions import IsAuthenticated
from habit.paginators import HabitPaginator
from users.models import UserRoles
from habit.services import send_habit_email, set_schedule


class HabitViewSet(ModelViewSet):
    """ViewSet для модели Habit, используется HabitSerializer, есть ограничение доступа только для авторизованных
    пользователей, настроена пагинация"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = HabitPaginator

    def perform_create(self, serializer):
        """Поле created_by автоматически заполняется при создании привычки
        в нем будет указан авторизованный пользователь"""
        serializer.save(created_by=self.request.user)
        habit = serializer.save()
        set_schedule(habit)
        send_habit_email(self.request.user.email)

    def get_queryset(self):
        """Получение списка привычек исходя из статуса и допуска пользователей"""
        user = self.request.user
        if user.is_superuser or user.is_staff or user.role == UserRoles.MODERATOR:
            return Habit.objects.all()
        else:
            return Habit.objects.filter(created_by=user)


class HabitIsPublicListAPIView(ListAPIView):
    """ListAPIView для получения привычек со статусом is_public=True"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = HabitPaginator

    def get_queryset(self):
        """Получение списка привычек исходя из статуса и допуска пользователей, а также статуса привычки"""
        user = self.request.user
        if user.is_superuser or user.is_staff or user.role == UserRoles.MODERATOR:
            return Habit.objects.all()
        else:
            return Habit.objects.filter(public=True)
