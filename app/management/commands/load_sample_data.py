from django.core.management.base import BaseCommand, CommandError
from app.models import *
import csv
import random

class Command(BaseCommand):
    help = 'Loads sample data'

    def handle(self, *args, **options):
        with open('user_sample_data.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for line in reader:
                User.objects.update_or_create(**line)

        with open('listing_sample_data.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for line in reader:
                if len(Listing.objects.filter(**line)) == 0:
                    #assign to a random user
                    user_id = random.choice(User.objects.all()).id
                    line['user_id'] = user_id
                    Listing.objects.create(**line)
