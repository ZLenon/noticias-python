from django.db import models

model_dj = models.Model


class Categories(model_dj):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name
