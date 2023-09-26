from django.db import models


class Categories(models.Model):
    x = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.x
