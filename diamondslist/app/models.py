from django.db import models

# Create your models here.

class User(models.Model):
    firstname = models.CharField(max_length=200, blank=True, null=True)
    lastname = models.CharField(max_length=200, blank=True, null=True)
    profile = models.TextField()

class Listing(models.Model):
    user = models.ForeignKey(User)
    
    LISTING_CATEGORIES = (
        ("AUTO", "Auto Repair"),
        ("LANDSCAPING", "Landscaping")
        )
    
    service_type = models.CharField(max_length=50, choices=LISTING_CATEGORIES, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    hourly_rate = models.IntegerField(blank=True, null=True)