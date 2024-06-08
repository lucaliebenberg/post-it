from django.db import models

class JobPost(models.Model):
    author = models.ForeignKey(
        "post author",
        on_delete=models.CASCADE,
        nul=False,
        blank=False,
    )
    title = models.CharField(
        "post title",
        max_length=255,
        nul=False,
        blank=False,
    )
