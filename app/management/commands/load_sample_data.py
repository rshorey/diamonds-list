from django.core.management.base import BaseCommand, CommandError
from app.models import *
import csv

class Command(BaseCommand):
    help = 'Loads sample data'

    def handle(self, *args, **options):
        with open('user_sample_data.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for line in reader:
                User.objects.update_or_create(**line)