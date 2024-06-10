from django.contrib import admin
from django.urls import path
from jobposts.views import (
    CreateJobPost,
    DeleteJobPost
)

app_name = "jobposts"

urlpatterns = [
    path('create/', CreateJobPost.as_view(), name="create_jobpost"),    
    path('delete/<int:pk>/', DeleteJobPost.as_view(), name="delete_jobpost"),    
]
