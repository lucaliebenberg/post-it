from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    CreateView, 
    UpdateView,
    DeleteView, 
    DetailView
)
from jobposts.models import JobPost

class DefaultView(TemplateView):
    template_name = "index.html"

class CreateJobPost(CreateView):
    model = JobPost
    template_name = "create_jobpost.html"
    fields = '__all__'
    success_url = 'index'
    