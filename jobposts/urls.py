from django.contrib import admin
from django.urls import path
from jobposts.views import CreateJobPost

app_name = "jobposts"

urlpatterns = [
    path('/jobpost', CreateJobPost.as_view(), name="create_jobpost"),    
]
