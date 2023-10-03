from django.db import models
from news.is_valid import is_valid_data, is_valid_title

model_dj = models.Model


class News(model_dj):
    title = models.CharField(max_length=200, validators=[is_valid_title])
    image = models.ImageField(upload_to="img/", null=True, blank=True)
    created_at = models.DateField(validators=[is_valid_data])
    categories = models.ManyToManyField(
        "Categories",
        related_name="news",
    )
    author = models.ForeignKey(
        "Users",
        on_delete=models.CASCADE,
        related_name="news",
    )
    content = models.TextField()

    def __str__(self) -> str:
        return self.title
