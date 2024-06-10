from django.forms import BaseModelForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy
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
    
    def get_context_data(self, **kwargs) -> dict[str]:
        context = super().get_context_data(**kwargs)
        job_posts = JobPost.objects.all()
        # print("Job Posts --> ", job_posts)
        context["posts"] = job_posts
        return context
    
class CreateJobPost(CreateView):
    model = JobPost
    template_name = "create_jobpost.html"
    fields = '__all__'
    success_url = reverse_lazy("index")

class DeleteJobPost(DeleteView):
    model = JobPost
    template_name = "delete_jobpost.html"
    fields = '__all__'
    success_url = reverse_lazy("index")