from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader
from app.models import *
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, login


def index(request):
    listings = Listing.objects.order_by('-created_date')[:10]
    context = {'listings': listings}
    if request.user.is_authenticated():
        context['user'] = request.user
    return render(request, 'index.html', context)

def listings(request):
    params = request.GET
    if 'q' in params:
        search_str = params['q']
        listing_list = Listing.objects.filter(Q(description__icontains=search_str)
                    | Q(title__icontains=search_str)
                    | Q(service_type__icontains=search_str)).order_by('-created_date')
    else:
        listing_list = Listing.objects.order_by('-created_date')
    
    page = params.get('page')
    per_page = params['per_page'] if 'per_page' in params else 10

    paginator = Paginator(listing_list, per_page)

    try:
        listings = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        listings = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        listings = paginator.page(paginator.num_pages)

    context = {'listings': listings}
    return render(request, 'listings.html', context)

def user(request, user_id):
    person = get_object_or_404(User, pk=user_id)
    return render(request, 'user.html', {'person': person, 'listings' : person.listing_set.all()})

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    return render(request, 'listing.html', {'listing': listing})

def about(request):
    return render(request, 'about.html')