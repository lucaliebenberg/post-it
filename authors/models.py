from django.db import models
from jobposts.models import JobPost

class Author(models.Model):
    posts = models.ForeignKey(
        JobPost,
        on_delete=models.CASCADE
    )
    name = models.CharField(
        "author name",
        max_length=255,
        null=False,
        blank=False
    )
