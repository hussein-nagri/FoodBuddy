from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    params = {"name" :"Hussein", "place" : "USA"}

    return render(request, "index.html", params)