"""Simple model."""
from django.db import models
import datetime

# Create your models here.


class Preson(models.Model):
    """Person model for first ticket."""

    name = models.CharField(max_length=60, blank=True)
    surname = models.CharField(max_length=60, blank=True)
    date_of_birth = models.DateField(default=datetime.date(1985, 10, 26))
    bio = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    jabber_id = models.CharField(max_length=60, blank=True)
    skype_id = models.CharField(max_length=60, blank=True)
    other_contacts = models.TextField(blank=True)
