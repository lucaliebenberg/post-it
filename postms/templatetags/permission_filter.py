from django import template
from jobposts.models import JobPost
from accounts.models import User

register = template.Library()

@register.filter
def is_post_author(user, post):
    return user == post.creator

