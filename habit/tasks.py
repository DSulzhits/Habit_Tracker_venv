from django.conf import settings
from telebot import TeleBot
from config.celery import app
from habit.models import Habit


@app.task
def send_tgbot_message(habit_id):
    """Задача для отправления сообщения телеграмм ботом настройки периодичности заданы в админке"""
    habit = Habit.objects.get(id=habit_id)
    tg_bot = TeleBot(settings.TG_BOT_TOKEN)
    message = f"Напоминаю время:{habit.time} для {habit.name}, надо сделать {habit.action}! Место {habit.place}."
    tg_bot.send_message(habit.created_by.telegram_id, message)
