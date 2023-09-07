from habit.apps import HabitConfig
from rest_framework.routers import DefaultRouter
from django.urls import path
from habit.views import HabitViewSet, HabitIsPublicListAPIView

app_name = HabitConfig.name

router = DefaultRouter()
router.register(r'habits', HabitViewSet, basename='habits')

urlpatterns = [
    path('habits_public/', HabitIsPublicListAPIView.as_view(), name='habits_is_public')
] + router.urls
