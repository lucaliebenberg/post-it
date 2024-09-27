from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path, include
from jobposts.views import DefaultView
from accounts.views import (
    CustomRegisterView,
    CustomLoginView,
    CustomLogoutView,
)

app_name = "postms"

# ERROR HANDLERS
# handler400 = "postms.views.handler400"
# handler403 = "postms.views.handler403"
# handler404 = "postms.views.handler404"
# handler500 = "postms.views.handler500"

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
] + static(
    settings.MEDIA_URL, 
    document_root=settings.MEDIA_ROOT
)


# PROJECT ADMIN SETTINGS CONFIG
admin.site.index_title = "PostIt"
admin.site.site_header = "PostIt Admin"
admin.site.site_title = "Self Service Job Post Portal"