"""Simple test."""
from django.test import TestCase, Client
from django.urls import reverse

# Create your tests here.


class PageTest(TestCase):
    """Simple view test."""

    def setUp(self):
        """Test needs a client."""
        self.client = Client()

    def test_index_page(self):
        """Check that responce is 200 ok, template used."""
        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
