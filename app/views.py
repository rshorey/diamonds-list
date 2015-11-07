from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader
from app.models import *

def index(request):
    listings = Listing.objects.order_by('-created_date')[:10]
    context = {'listings': listings}
    return render(request, 'index.html', context)

def listings(request):
    listings = Listing.objects.order_by('-created_date')
    context = {'listings': listings}
    return render(request, 'listings.html', context)

def user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'user.html', {'user': user, 'listings' : user.listing_set.all()})

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    return render(request, 'listing.html', {'listing': listing})
