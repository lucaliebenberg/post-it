from django import template
from jobposts.models import JobPost

register = template.Library()

@register.filter
def is_post_author(user, post):
    return user == post.creator

@register.filter
def check_user_total_posts(user, post):
    posts_qs= JobPost.objects.all().filter(creator=user)
    posts = list(posts_qs)
    if len(posts) >= 1:
        return False
    return True

@register.filter
def check_reference_jobpost_creator(user, post):
    post = JobPost.objects.get(creator=user)
    if user.pk == post.creator.pk:
        return True
    return False
