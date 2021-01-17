from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'photomatch/index.html')


def landing(request):
    return render(request, 'photomatch/landing_page.html')

