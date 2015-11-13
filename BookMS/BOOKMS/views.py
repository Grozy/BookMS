from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import  HttpResponse
# Create your views here.
def hello(request):
    return HttpResponse("Hello world")

def login(request):
    return render_to_response("login.html")