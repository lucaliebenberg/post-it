from django.contrib import admin
from accounts.models import User

@admin.register(User)
class AuthorAdmin(admin.ModelAdmin):
    list_display =(
        "username",
        "email",
        "contact_num",
        "is_staff",
        "is_active",
        "date_joined",
    )