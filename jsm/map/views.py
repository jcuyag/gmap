import json

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

from .map_api import google

def index(request):
    
    if request.method == 'POST':
        # print(dir(request.POST))
        for i in request.POST.items():
            print(i)
        
            CONTEXT = {
                'searched': request.POST.get('search_name'),
            }
    elif request.method == 'GET':
        CONTEXT = {
            'searched': ''
        }
    return render(request, 'index.html', context=CONTEXT)


def store_data(request, key_place):
    print(key_place)

    _google = google.GooglePlaces()
    data = _google.get_restaurants(key_place)
    _data = json.loads(json.dumps(data))
    
    return JsonResponse(_data)


def restau_img(request):
    image_data = open("map/static/img/restaurant.png", "rb").read()
    return HttpResponse(image_data, content_type="image/png")

def specialty_img(request):
    image_data = open("map/static/img/specialty.jpg", "rb").read()
    return HttpResponse(image_data, content_type="image/png")

