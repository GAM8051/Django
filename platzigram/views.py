"""Platzigram views"""

#Django
from django.http import HttpResponse

#Utilities
from datetime import date, datetime
import json

def hello_world(request):
    """Return a greeting"""
    return HttpResponse("Oh, hi! Current server time is {now}".format(now = datetime.now().strftime("%b %dth, %Y - %H:%M hrs")))

def sort_integers(request):
    """Return a JSON response with sorted integers (http://localhost:8000/sorted/?numbers=55,68,98,16)"""
    numbers = [int(i) for i in request.GET["numbers"].split(",")]
    sorted_ints = sorted(numbers)
    data = {
        "status": "ok",
        "numbers": sorted_ints,
        "message": "Integers sorted successfully."
    }
    return HttpResponse(
        json.dumps(data, indent=4),
        content_type="application/json"
        )

def say_hi(request, name, age):
    """Return a greeting (http://localhost:8000/hi/julian/10/)"""
    if age < 12:
        message = "Sorry {}, you are not allowed here".format(name)
    else:
        message = "Hello, {}! Welcome to Platzigram".format(name)
    return HttpResponse(message)
