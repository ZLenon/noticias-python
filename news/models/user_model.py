from django.db import models

model_dj = models.Model


class Users(model_dj):
    password = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    role = models.CharField(max_length=200)
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name
