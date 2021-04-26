from django.core.exceptions import ValidationError


def score_validator(value):
    if not 1 <= value <= 10:
        params = {'value': value, }
        raise ValidationError('Оценка может быть от 1 до 10', params=params)