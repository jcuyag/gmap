import json

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse


def index(request):
    return render(request, 'index.html')


def store_data(request):
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
