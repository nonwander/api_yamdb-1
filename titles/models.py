from titles.validators import year_validator
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, max_length=100)


class Genre(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, max_length=100)

    class Meta:
        ordering = ['-name']

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(max_length=200)
    year = models.PositiveIntegerField(null=True, 
                                       blank=True, 
                                       validators=[year_validator], 
                                       db_index=True)
    description = models.CharField(max_length=400, blank=True)
    category = models.ForeignKey(Category,
                                 blank=True,
                                 null=True,
                                 on_delete=models.SET_NULL,
                                 related_name='titles')
    genre = models.ManyToManyField(Genre, blank=True)

    class Meta:
        ordering = ['-name']

    def __str__(self):
        return self.name
