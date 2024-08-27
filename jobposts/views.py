from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    CreateView, 
    DeleteView, 
    DetailView,
    ListView
)
from jobposts.forms import JobPostForm
from jobposts.models import JobPost
from references.models import Reference

@method_decorator(login_required, name="dispatch")
class DefaultView(ListView):
    model = JobPost
    template_name = "index.html"
    paginate_by = 9
    
    def get_context_data(self, **kwargs) -> dict[str]:
        context = super(DefaultView, self).get_context_data(**kwargs)
        job_posts_total_qs = JobPost.objects.all()
        job_posts_total = len(list(job_posts_total_qs))
        job_posts = context['object_list']
        current_user = self.request.user
        for post in job_posts:
            creator = post.creator
            context['post'] = post
            context['creator'] = creator
        context["posts"] = job_posts
        context["current_user"] = current_user
        context["total_posts"] = job_posts_total
        return context
    
@method_decorator(login_required, name="dispatch")
class CreateJobPost(CreateView):
    model = JobPost
    form_class = JobPostForm
    template_name = "create_jobpost.html"
    success_url = reverse_lazy("index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        context['post'] = post
        return context
    
    def form_valid(self, form):
        form.instance.creator = self.request.user
        self.object = form.save()
        Reference.objects.create(
            job_post=self.object,
            name=form.cleaned_data['reference_name_1'],
            number=form.cleaned_data['reference_number_1']
        )
        Reference.objects.create(
            job_post=self.object,
            name=form.cleaned_data['reference_name_2'],
            number=form.cleaned_data['reference_number_2']
        )
        return HttpResponseRedirect(reverse_lazy("index"))
    
class CreateReference(CreateView):
    model = Reference
    template_name = "create_jobpost.html"
    fields = (
        "name",
        "number"
    )
    success_url = reverse_lazy("index")


@method_decorator(login_required, name="dispatch")
class DetailView(DetailView):
    model = JobPost
    template_name = "detail_jobpost.html"
    fields = '__all__'

    def get_context_data(self, **kwargs) -> dict[str]:
        context =  super().get_context_data(**kwargs)
        post = self.get_object()
        user = self.request.user
        references_qs = Reference.objects.all().filter(job_post=post)
        references = list(references_qs)
        context['post'] = post
        context['user'] = user
        context['references'] = references
        return context

@method_decorator(login_required, name="dispatch")
class DeleteJobPost(DeleteView):
    model = JobPost
    template_name = "delete_jobpost.html"
    fields = '__all__'
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs) -> dict[str]:
        context =  super().get_context_data(**kwargs)
        post = self.get_object
        context['post'] = post
        return context