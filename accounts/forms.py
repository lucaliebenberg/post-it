from django import forms
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    UserChangeForm,
    PasswordChangeForm,
    PasswordResetForm
)
from django.contrib.auth import get_user_model, get_user

User = get_user_model

class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        max_length=60 , 
        help_text=("Required. Add a valid email address")
    )

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "is_staff",
            "is_active",
            "password1",
            "password2"
        ]

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ["username", "password"]