from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

NULLABLE = {'blank': True, 'null': True}


class UserRoles(models.TextChoices):
    MEMBER = 'member', _('member')
    MODERATOR = 'moderator', _('moderator')


class User(AbstractUser):
    """Модель пользователя"""
    username = None
    email = models.EmailField(unique=True, verbose_name='email')
    role = models.CharField(max_length=9, choices=UserRoles.choices, default=UserRoles.MEMBER)
    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/avatars/', verbose_name='аватар', **NULLABLE)
    telegram_id = models.CharField(max_length=15, verbose_name='id телеграм', **NULLABLE)
    is_active = models.BooleanField(default=True, verbose_name="активный")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['id']
