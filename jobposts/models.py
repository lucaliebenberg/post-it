from django.db import models
from accounts.models import User

class JobPost(models.Model):
    creator = models.ForeignKey(
       User,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    contact_num = models.CharField(
        "author contact number",
        max_length=255,
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
