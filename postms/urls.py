from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from jobposts.views import DefaultView
from accounts.views import (
    CustomRegisterView,
    CustomLoginView,
    CustomLogoutView,
    CustomResetPasswordView
)

# ERROR HANDLERS
# handler400 = "path"
# handler403 = "path"
# handler404 = "path"
# handler500 = "path"

app_name = "postms"

urlpatterns = [
    # ADMIN
    path('admin/', admin.site.urls),

    # AUTH (USER)
    path('register', CustomRegisterView.as_view(), name="register"),
    path('login', CustomLoginView.as_view(), name="login"),
    path('logout', CustomLogoutView.as_view(), name="logout"),
    

    # CLIENT
    path('', DefaultView.as_view(), name="index"),
    path('jobposts/', include("jobposts.urls")),
    path('account/', include("accounts.urls")),
]


# PROJECT ADMIN SETTINGS CONFIG
# admin.site.index.title = "PostIt"
# admin.site.site_header = "PostIt Admin"
# admin.site.site_title = "Self Service Job Post Portal"