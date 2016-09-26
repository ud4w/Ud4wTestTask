"""Simple test."""
from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from models import Person
import datetime

# Create your tests here.


class PageTest(TestCase):
    """Simple view test."""

    def setUp(self):
        """Test needs a client."""
        self.client = Client()

    def test_index_page(self):
        """Check that responce is 200 ok, template used."""
        url = reverse('udaw_test:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')


class PersonTest(TestCase):
    """Simple maodel test."""

    def setUp(self):
        """Setting person for testing purpose."""
        self.def_person = Person.objects.create()

    def test_person_name(self):
        """Rich test for default person birth date is not in the future."""
        self.assertIs(
            self.def_person.date_of_birth <= datetime.datetime.now().date(),
            True)
