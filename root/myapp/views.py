from django.shortcuts import render, HttpResponse
import datetime

# Create your views here.

def say_hello(request):
    now_time = str(datetime.datetime.now())
    name = request.GET.get('name')
    if not name:
        name = "GUEST"
    return HttpResponse(
        "<h1>Hello {}</h1>".format(name) + "<br /><br />" + now_time
    )