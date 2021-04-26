from django.contrib.auth.models import AbstractUser
from django.db import models


ROLE = [
    ('user', 'user'),
    ('moderator', 'moderator'),
    ('admin', 'admin'),
]


class CustomUser(AbstractUser):
    ROLE_USER = 'user'
    ROLE_MODERATOR = 'moderator'
    ROLE_ADMIN = 'admin'
    USERS_ROLE = (
        (ROLE_USER, 'Пользователь'),
        (ROLE_MODERATOR, 'Модератор'),
        (ROLE_ADMIN, 'Админ'),
    )

    role = models.CharField(
        choices=USERS_ROLE,
        max_length=10,
        verbose_name='Роль пользователя',
        default='user'
    )
    email = models.EmailField('e-mail', unique=True)
    bio = models.TextField(
        max_length=500,
        blank=True,
        null=True,
    )

    @property
    def is_admin(self):
        return self.role == self.role('admin')
    
    @property
    def is_moderator(self):
        return self.role == self.role('moderator')

    def __str__(self):
        return self.email


class ConfirmationCode(models.Model):
    confirmation_code = models.CharField(max_length=32)
    email = models.EmailField(max_length=254, unique=True)
    code_date = models.DateTimeField(auto_now_add=True)
