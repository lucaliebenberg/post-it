from django.urls import path
from django.contrib.auth import views as auth_views
from accounts.views import (
    AccountMenuView
)
from accounts.views import (
    CustomResetPasswordView
)

app_name = "accounts"

urlpatterns = [
    path(
        'password-reset', 
        CustomResetPasswordView.as_view(), 
        name="reset_password"
    ),
    path(
        'password-reset-confirm/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(
            template_name="password_reset_confirm.html"
            ), 
        name="password_reset_confirm"
    ),
     path(
        'password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
            template_name='password_reset_complete.html'
            ),
         name='password_reset_complete'
        ),

    path(
        "account/menu/",
        AccountMenuView.as_view(), 
        name="account_menu"
    )
]
