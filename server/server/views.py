from random import random as _random
from django.shortcuts import render
from django.http import JsonResponse


def index(request):
    return render(request, 'index.html')


def random(request):
    return JsonResponse({'random': _random()})
