from django.contrib import admin
from django.urls import path
from jobposts.views import (
    CreateJobPost,
    DetailView,
    DeleteJobPost,
    UpdateJobPost
)

app_name = "jobposts"

urlpatterns = [
    path('create/', CreateJobPost.as_view(), name="create_jobpost"),     
    path('delete/<int:pk>/', DeleteJobPost.as_view(), name="delete_jobpost"),
    path('update/<int:pk>/', UpdateJobPost.as_view(), name="update_jobpost"),
    path('detail/<int:pk>/', DetailView.as_view(), name="detail_jobpost"),    
]
