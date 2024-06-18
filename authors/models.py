from django.db import models
from jobposts.models import JobPost
from accounts.models import User

class Author(models.Model):
    posts = models.ForeignKey(
        JobPost,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )
