""""Simple view."""
from django.shortcuts import render
from models import Person
# Create your views here.


def index(request):
    """Person view."""
    person = Person.objects.get(pk=1)
    context = {'person': person}
    return render(request, 'index.html', context)
