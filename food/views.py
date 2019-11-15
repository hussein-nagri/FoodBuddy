from django.shortcuts import render
from math import ceil
import datetime 
from .models import Food

# Create your views here.
from django.http import HttpResponse

def index(request):

    allProds = []
    name = Food(food_name="apples",
              food_amount = 3,
              date = (11/2/4) )
    print(name.food_amount)
    params = {'allProds':allProds}
    return render(request, 'food/index.html', params)

def about(request):
    return render(request, 'shop/about.html')

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
