"""Simple test."""
from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from models import Person

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


class PersonTest(TestCase):
    """Simple maodel test."""

    def setUp(self):
        """Setting person to test."""
        self.person = Person.objects.filter(pk=1)

    def test_person_name(self):
        """Testting that name first letter should be uppercase."""
        self.assertEqual(
            self.person.__unicode__(), self.person.__unicode__().title())
