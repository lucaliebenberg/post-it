from django.contrib import admin
from jobposts.models import JobPost

@admin.register(JobPost)
class JobPostAdmin(admin.ModelAdmin):
    list_display =(
        # "creator",
        "title",
        "description",
        "created_at"
    )