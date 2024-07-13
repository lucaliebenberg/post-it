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

@method_decorator(login_required, name="dispatch")
class DefaultView(TemplateView):
    template_name = "index.html"
    
    def get_context_data(self, **kwargs) -> dict[str]:
        context = super(DefaultView, self).get_context_data(**kwargs)
        job_posts = JobPost.objects.all()
        current_user = self.request.user

        for post in job_posts:
            creator = post.creator
            context['post'] = post
            context['creator'] = creator
            print("Post creator >> ", post.creator)

        context["posts"] = job_posts
        context["current_user"] = current_user

        return context
    
@method_decorator(login_required, name="dispatch")
class CreateJobPost(CreateView):
    model = JobPost
    template_name = "create_jobpost"
    fields = (
        "contact_num",
        "title",
        "description",
    )
    success_url = reverse_lazy("index")
    
    def form_valid(self, form):
        form.instance.creator = self.request.user
        self.object = form.save()

        return HttpResponseRedirect(reverse_lazy("index"))
    

@method_decorator(login_required, name="dispatch")
class DetailView(DetailView):
    model = JobPost
    template_name = "detail_jobpost"
    fields = '__all__'

    def get_context_data(self, **kwargs) -> dict[str]:
        context =  super().get_context_data(**kwargs)
        post = self.get_object
        user = self.request.user
        context['post'] = post
        context['user'] = user
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
    