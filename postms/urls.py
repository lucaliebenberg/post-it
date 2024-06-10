from django.contrib import admin
from django.urls import path, include
from jobposts.views import DefaultView

# ERROR HANDLERS
# handler400 = "path"
# handler403 = "path"
# handler404 = "path"
# handler500 = "path"

app_name = "postms"

urlpatterns = [
    # ADMIN
    path('admin/', admin.site.urls),

    # CLIENT
    path('', DefaultView.as_view(), name="index"),
    path('jobposts/', include("jobposts.urls")),
]


# PROJECT ADMIN SETTINGS CONFIG
# admin.site.index.title = "PostIt"
# admin.site.site_header = "PostIt Admin"
# admin.site.site_title = "Self Service Job Post Portal"