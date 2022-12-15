from django.db import models


class Album(models.Model):
    class Meta:
        ordering = ["id"]

    name = models.CharField(max_length=255, blank=False, null=False)
    year = models.PositiveSmallIntegerField(blank=False, null=False)

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="albums",
    )
