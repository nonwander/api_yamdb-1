from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from api_users_auth.models import CustomUser
from titles.models import Title


class Review(models.Model):
    score = models.IntegerField(
        validators=[
            MinValueValidator(1, message='Введите число не меньше 1'),
            MaxValueValidator(10, message='Введите число не больше 10')],
        blank=True, null=True)
    text = models.TextField('Текст', blank=True, null=True)
    pub_date = models.DateTimeField(
        'Дата отзыва',
        auto_now_add=True,
        db_index=True,
    )
    author = models.ForeignKey(
        CustomUser,
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


class Comment(models.Model):
    text = models.TextField('Комментарий', blank=True, null=True)

    author = models.ForeignKey(
        CustomUser,
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
