from django.test import TestCase
from django.urls import reverse

class WikiTests(TestCase):
    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertContains(response, "Welcome to Wiki!")


