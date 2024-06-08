from django.db import models

class JobPost(models.Model):
    author = models.CharField(
        "post author",
        null=False,
        blank=False,
    )
    title = models.CharField(
        "post title",
        max_length=255,
        null=False,
        blank=False,
    )
    description = models.CharField(
        "post description",
        max_length=255,
        null=False,
        blank=False,
    )
    created_at = models.DateTimeField(
        "date posted",
        editable=False,
        auto_now=True,
    )
