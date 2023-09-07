from django.core.mail import send_mail
from django.conf import settings
from django_celery_beat.models import CrontabSchedule, PeriodicTask


def send_habit_email(email):
    send_mail(
        subject='Новая привычка',
        message='Поздравляем! Вы добавили себе новую полезную привычку! Так держать!',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email]
    )


def set_schedule(habit):
    """Задает периодичность и отправляет задачу на отправку"""
    crontab_schedule, _ = CrontabSchedule.objects.get_or_create(
        minute=habit.time.minute,
        hour=habit.time.hour,
        day_of_month=f'*/{habit.periodic}',
        month_of_year='*',
        day_of_week='*',
    )

    PeriodicTask.objects.create(
        crontab=crontab_schedule,
        name=f'Habit Task - {habit.name}',
        task='habit.tasks.send_tgbot_message',
        args=[habit.id],
    )
