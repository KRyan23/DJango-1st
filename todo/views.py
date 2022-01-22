from django.shortcuts import render, HttpResponse

# Create your tests here.

def sayhello(request):
    return HttpResponse("hello")