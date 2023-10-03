from django.core.exceptions import ValidationError
from datetime import datetime


def is_valid_data(value):
    try:
        datetime.strptime(str(value), "%Y-%m-%d")

        return True
    except ValueError:
        raise ValidationError(
            "Use o formato AAAA-MM-DD e uma data igual ou anterior a hoje."
        )


def is_valid_title(value):
    if not len(str(value).split()) > 1:
        raise ValidationError("O título deve conter pelo menos 2 palavras.")
