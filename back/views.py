from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse

from back.data import getData


def connection(request):
    list = getData()
    print(list)
    data = {
        'n': 3,
        'scores': list
    }

    return JsonResponse(data)