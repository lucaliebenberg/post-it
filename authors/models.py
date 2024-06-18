from django.db import models
from accounts.models import User

class Author(models.Model):
    posts = models.ForeignKey(
        "jobposts.JobPost",
        on_delete=models.CASCADE,
        null=True,
        blank=False,
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )
