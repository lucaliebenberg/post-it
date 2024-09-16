from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView
)
from references.models import Reference

class CreateReference(CreateView):
    model = Reference
    template_name = "create_jobpost.html"
    fields = (
        "name",
        "number"
    )
    success_url = reverse_lazy("index")

