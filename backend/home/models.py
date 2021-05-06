from django.conf import settings
from django.db import models


class Images(models.Model):
    "Generated Model"
    imageUrl = models.URLField()
    userPics = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="images_userPics",
    )
