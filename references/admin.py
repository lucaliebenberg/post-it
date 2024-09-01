from django.contrib import admin
from references.models import Reference

@admin.register(Reference)
class ReferencesAdmin(admin.ModelAdmin):
    list_display =(
        "job_post",
        "name",
        "number",
    )