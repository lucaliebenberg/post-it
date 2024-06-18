from django.test import TestCase
from jobposts.models import JobPost

class JobPostTestCase(TestCase):
    def setup(self):
        JobPost.objects.create(creator='182', contact_num="09872612431",
            title="Marketing Guru",
            description="This is a hello world test",
        )
        
    def test_animal_creation(self):
        post = JobPost.objects.get(title='Marketing Guru')
        self.assertEqual(post.title, "Marketing Guru")
