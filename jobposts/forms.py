from django import forms
from django.forms import ModelForm
from jobposts.models import JobPost

class JobPostForm(ModelForm):
    reference_name_1 = forms.CharField(max_length=255, required=False)
    reference_number_1 = forms.CharField(max_length=255, required=False)
    reference_name_2 = forms.CharField(max_length=255, required=False)
    reference_number_2 = forms.CharField(max_length=255, required=False)

    class Meta:
        model = JobPost
        fields = [
            'contact_num', 
            'title', 
            'description',
            'image'
        ]
