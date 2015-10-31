from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. This is the front page of Diamond's List.")

def user(request, user_id):
    return HttpResponse("This is the page for user {}".format(user_id))

def listing(request, listing_id):
    return HttpResponse("This is the page for listing {}".format(listing_id))