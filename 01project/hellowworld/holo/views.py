from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def homepageview(request):
    return HttpResponse('holo means hello in spanish')
