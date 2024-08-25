from django import template
from jobposts.models import JobPost
from accounts.models import User

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
