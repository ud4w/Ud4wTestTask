""""Simple view."""
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from models import Person

# Create your views here.


def index(request):
    """Person view."""
    try:
        person = Person.objects.get(pk=1)
    except ObjectDoesNotExist:
        person = None
    return render(request, 'index.html', {'person': person})
