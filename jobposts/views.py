from django.forms import BaseModelForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    TemplateView,
    CreateView, 
    DeleteView, 
    DetailView
)
from jobposts.models import JobPost
from accounts.models import User
from accounts.constants import LOG_OUT_VIA

@method_decorator(login_required, name="dispatch")
class DefaultView(TemplateView):
    template_name = "index.html"
    
    def get_context_data(self, **kwargs) -> dict[str]:
        context = super(DefaultView, self).get_context_data(**kwargs)
        job_posts = JobPost.objects.all()
        users = User.objects.all()
        for post in job_posts:
            context['post'] = post

        context["posts"] = job_posts
        print("posts --> ", job_posts)
        print("users --> ", users)

        return context
    
@method_decorator(login_required, name="dispatch")
class CreateJobPost(CreateView):
    model = JobPost
    template_name = "create_jobpost"
    fields = '__all__'
    success_url = reverse_lazy("index")

@method_decorator(login_required, name="dispatch")
class DetailView(DetailView):
    model = JobPost
    template_name = "detail_jobpost"
    fields = '__all__'

    def get_context_data(self, **kwargs) -> dict[str]:
        context =  super().get_context_data(**kwargs)
        post = self.get_object
        context['post'] = post
        print('Post --> ', post)
        return context

@method_decorator(login_required, name="dispatch")
class DeleteJobPost(DeleteView):
    model = JobPost
    template_name = "delete_jobpost"
    fields = '__all__'
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs) -> dict[str]:
        context =  super().get_context_data(**kwargs)
        post = self.get_object
        context['post'] = post
        return context
    
    def get_success_url(self) -> str:
        return super().get_success_url()
    