from django.db import models
from datetime import datetime
from django.conf import settings
from django.contrib.auth.models import User




class Service(models.Model):
    last_modified = models.DateTimeField(auto_now=True) 
    CLUB_CHOICES = (
        ('G', 'General'),
        ('K', 'Key Club'),
    )
    club = models.TextField(db_index=True, choices=CLUB_CHOICES, default='G')
    contactName = models.TextField()
    contactPhone = models.TextField()
    dateCompleted = models.DateField(auto_now=True)
    description = models.TextField()
    hours = models.DecimalField(max_digits=6, decimal_places=2)
    accurate = models.BooleanField()
    performedByID = models.ForeignKey(User, on_delete=models.CASCADE)
      