from django import template
from jobposts.models import JobPost
from accounts.models import User

register = template.Library()

@register.filter
def is_post_author(user, post):
    # post = JobPost.objects.get(pk=self.kwargs.get("pk"))
    # post_creator = User.objects.get(email=post.creator)
    # print("Post creator >>> ", post_creator)
    # user = self.request.user
    # print("Current user >>> ", user)
    # if self.request.user is post_creator:
    #     print(
    #     """
    #     This is the owner of the job post
    #     """
    #     )
    #     return True
    # else: 
    #     raise Exception("User is not post author!!!")
    return user == post.creator

