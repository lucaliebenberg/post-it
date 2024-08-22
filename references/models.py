from django.db import models
from jobposts.models import JobPost

class Reference(models.Model):
    job_post = models.ForeignKey(
        JobPost,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    name = models.CharField(
        "reference full name",
        max_length=255,
        null=False,
        blank=False,
    )
    number = models.CharField(
        "reference contact number",
        max_length=255,
        null=False,
        blank=False,
    )
