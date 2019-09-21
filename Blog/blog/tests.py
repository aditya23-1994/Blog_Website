from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Post

# Create your tests here.

class BlogTestCase(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.Create(
           username='testuser',
           email= 'test@email.com',
           password = 'secret'

        )
    
    self.post = Post.objects.Create(
        title = 'A good title',
        body = 'Nice body content',
        author = self.user,
    )

    def test_String_representation(self):

        post = Post(title='A sample title')
        self.assertEqual(str(post), post.title)
        