""""Simple view."""
from django.shortcuts import render
from models import Person

# Create your views here.


def index(request):
    """Person view."""
    person = Person.objects.get(pk=1)
    return render(request, 'index.html', {'person': person})


def requests(request):
    """Request view."""
    return render(request, 'requests.html')
