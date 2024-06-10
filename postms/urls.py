from django.contrib import admin
from django.urls import path
from jobposts.views import DefaultView

urlpatterns = [
    path('', DefaultView.as_view(), name="index"),
    path('admin/', admin.site.urls),
]
