from django import template
# from jobposts.models import JobPost

register = template.Library()

def is_post_author(self):
    post_creator = self.JobPost.creator
    print("Post creator >>> ", post_creator)
    user = self.request.user
    print("Current user >>> ", user)
    if user is post_creator:
        print(
        """
        This is the owner of the job post
        """
        )
        return True
    else: 
        raise Exception("User is not post author!!!")

