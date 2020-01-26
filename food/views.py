from django.shortcuts import render
from math import ceil
import datetime 
from .models import Food
from .firebase import updateSQL
# Create your views here.
from django.http import HttpResponse

def index(request):

    allFoods = updateSQL()
    params = {'allFoods' : allFoods}
    print(allFoods)
    return render(request, 'food/index.html', params)

def about(request):
    return render(request, 'food/about.html')

def contact(request):
    return HttpResponse("We are at contact")



def tracker(request):
    return HttpResponse("We are at tracker")

def search(request):
    return HttpResponse("We are at search")

def productView(request):
    return HttpResponse("We are at product view")

def checkout(request):
    return HttpResponse("We are at checkout")
