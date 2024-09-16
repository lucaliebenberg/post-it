from django.contrib import admin
from django.urls import path
from references.views import (
    CreateReference
)

app_name = "references"

urlpatterns = [
    path('reference/', CreateReference.as_view(), name="create_reference"),    
]
