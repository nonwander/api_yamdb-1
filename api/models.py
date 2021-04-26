from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Avg
from .validators import score_validator
from titles.models import Title


class Roles(models.TextChoices):
    USER = 'user', 'Пользователь'
    MODERATOR = 'moderator', 'Модератор'
    ADMIN = 'admin', 'Администратор'

class User(AbstractUser):
    bio = models.TextField('О себе', blank=True, null=True, )
    email = models.EmailField('Email', unique=True)
    role = models.CharField('Роль', max_length=10, choices=Roles.choices,
                            default=Roles.USER)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('username',)


class Review(models.Model):
    score = models.PositiveSmallIntegerField(
        'Оценка',
        choices=[(r, r) for r in range(1, 11)],
        validators=[score_validator],
    )
    text = models.TextField('Текст', blank=True, null=True)
    pub_date = models.DateTimeField(
        'Дата отзыва',
        auto_now_add=True,
        db_index=True,
    )
    author = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.CASCADE,
    )
    title = models.ForeignKey(
        Title,
        related_name='reviews',
        verbose_name='Произведение',
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ('-pub_date',)

    def __str__(self):
        return self.text

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.score_avg = Review.objects.filter(title_id=self.title).aggregate(
            Avg('score')
        )
        self.title.rating = self.score_avg['score__avg']
        self.title.save()


class Comment(models.Model):
    text = models.TextField('Комментарий', blank=True, null=True)

    author = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.CASCADE,
    )
    pub_date = models.DateTimeField(
        'Дата',
        db_index=True,
        auto_now_add=True,
    )

    review = models.ForeignKey(
        Review,
        related_name='comments',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name='Комментарий'
    )

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ('-pub_date',)

    def __str__(self):
        return self.text