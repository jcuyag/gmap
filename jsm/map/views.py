import json

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse


def index(request):
    
    if request.method == 'POST':
        # print(dir(request.POST))
        for i in request.POST.items():
            print(i)
        
            CONTEXT = {
                'searched': request.POST.get('search_name'),
                'map_id':1
            }
    elif request.method == 'GET':
        CONTEXT = {
            'searched': request.POST.get('search_name')
        }
    return render(request, 'index.html', context=CONTEXT)


def store_data(request, _id):
    print(_id)
    _data = json.load(open('map/static/stores.json'))

    return JsonResponse(_data)


def cafe_img(request):
    image_data = open("map/static/img/icon_cafe.png", "rb").read()
    return HttpResponse(image_data, content_type="image/png")

def patte_img(request):
    image_data = open("map/static/img/icon_patisserie.png", "rb").read()
    return HttpResponse(image_data, content_type="image/png")

def cafe_logo(request):
    image_data = open("map/static/img/logo_cafe.png", "rb").read()
    return HttpResponse(image_data, content_type="image/png")

def patte_logo(request):
    image_data = open("map/static/img/logo_patisserie.png", "rb").read()
    return HttpResponse(image_data, content_type="image/png")
