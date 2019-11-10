from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    params = {"name" :"BOB", "place" : "USA"}

    return render(request, "index.html", params)