from django.forms import BaseModelForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    CreateView, 
    DeleteView, 
    DetailView
)
from jobposts.models import JobPost

class DefaultView(TemplateView):
    template_name = "index.html"
    
    def get_context_data(self, **kwargs) -> dict[str]:
        context = super().get_context_data(**kwargs)
        job_posts = JobPost.objects.all()
        for post in job_posts:
            print(f"""
                Post ID: {post.id},
                Post PK: {post.pk},
                Post Title: {post.title},
            """)
            
        context["posts"] = job_posts
        return context
    
class CreateJobPost(CreateView):
    model = JobPost
    template_name = "create_jobpost"
    fields = '__all__'
    success_url = reverse_lazy("index")

class DetailView(DetailView):
    model = JobPost
    template_name = "detail_jobpost"
    fields = '__all__'

    def get_context_data(self, **kwargs) -> dict[str]:
        context =  super().get_context_data(**kwargs)
        post = self.get_object
        print('Post --> ', post)
        # print('Post ID --> ', post.id)
        # print('Post PK --> ', post.pk)
        return context

class DeleteJobPost(DeleteView):
    model = JobPost
    template_name = "delete_jobpost"
    fields = '__all__'
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs) -> dict[str]:
        context =  super().get_context_data(**kwargs)
        post_pk = self.object.jobpost.pk
        # print('Post pk --> ', post_pk)
        return context
    
    def get_success_url(self) -> str:
        return super().get_success_url()
    