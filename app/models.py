from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Profile(models.Model):
    user = models.OneToOneField(User)
    profile = models.TextField()
    certifications = models.TextField(blank=True, null=True)
    num_jobs_completed = models.IntegerField(default=0) #will eventually be calculated, but this works for now
    def __str__(self):
        return "{} {}".format(self.firstname, self.lastname)

class Listing(BaseModel):
    user = models.ForeignKey(User)
    
    LISTING_CATEGORIES = (
        ("AUTO", "Auto Repair"),
        ("LANDSCAPING","Landscaping"),
        ("TECH", "Technology"),
        ("CREATIVE", "Creative and Design"),
        ("COACHING", "Coaching/Tutoring")

        )
    
    service_type = models.CharField(max_length=50, choices=LISTING_CATEGORIES, blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    hourly_rate = models.IntegerField(blank=True, null=True)
    has_references = models.NullBooleanField()

    def __str__(self):
        if self.title:
            return self.title
        else:
            return str(self.id)