import datetime

from django.core.exceptions import ValidationError


def year_validator(year):
    current_year = datetime.datetime.now().year
    if year > current_year:
        raise ValidationError(
            'Укажите правильный год. Указанный год больше текущего.')
