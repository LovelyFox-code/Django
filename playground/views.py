import re
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# request -> response
# request handler
# action (view)


def say_hello(request):
    # Pull data from dt
    # Transform
    # Send email
    return HttpResponse('Hello world')
