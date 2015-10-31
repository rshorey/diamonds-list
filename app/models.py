from django.db import models

# Create your models here.

class User(models.Model):
    firstname = models.CharField(max_length=200, blank=True, null=True)
    lastname = models.CharField(max_length=200, blank=True, null=True)
    profile = models.TextField()

    def __str__(self):
        return "{} {}".format(self.firstname, self.lastname)

class Listing(models.Model):
    user = models.ForeignKey(User)
    
    LISTING_CATEGORIES = (
        ("AUTO", "Auto Repair"),
        ("LANDSCAPING","Landscaping")
        )
    
    service_type = models.CharField(max_length=50, choices=LISTING_CATEGORIES, blank=True, null=True)
    title = models.CharField(max_length=20, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    certifications = models.TextField(blank=True, null=True)
    hourly_rate = models.IntegerField(blank=True, null=True)
    has_references = models.NullBooleanField()

    def __str__(self):
        if self.title:
            return self.title
        else:
            return str(self.id)