from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class CustomUser(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
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
    #username = None
    #objects = UserManager()

    @property
    def is_admin(self):
        return self.role == self.ROLE_ADMIN
    
    @property
    def is_moderator(self):
        return self.role == self.ROLE_MODERATOR

    def __str__(self):
        return self.email


class ConfirmationCode(models.Model):
    confirmation_code = models.CharField(max_length=32)
    email = models.EmailField(max_length=254, unique=True)
    code_date = models.DateTimeField(auto_now_add=True)
