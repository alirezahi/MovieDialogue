from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def dialogue_res(request):
    return HttpResponse('<div>hello world</div>')