""""Simple view."""
from django.shortcuts import render

# Create your views here.


def index(request):
    """Person view."""
    return render(request, 'index.html')
