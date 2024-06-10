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

    # def form_valid(self, form: BaseModelForm) -> HttpResponse:
    #     post = JobPost.objects.get(pk=self.kwargs.get("pk"))
    #     self.object = form.save()
    #     return HttpResponseRedirect(
    #         reverse("index")
    #     )

    # def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
    #     # context = super().get_context_data(**kwargs)
    #     # post = JobPost.objects.get(pk=self.kwargs.get("pk"))
    #     # context["post"] = post
    #     pass