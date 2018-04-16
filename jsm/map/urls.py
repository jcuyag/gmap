from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('data/<str:key_place>/', views.store_data, name='store_data'),
    path('index', views.index, name='index'),
    # restau_img
    path('img/restaurant', views.restau_img, name='restau_img'),
    path('img/specialty', views.specialty_img, name='special_img'),
    
    # path('img/icon_cafe', views.cafe_img, name='icon_cafe'),
    # path('img/icon_patisserie', views.patte_img, name='icon_patisserie'),
    # path('img/logo_cafe', views.cafe_logo, name='logo_cafe'),
    # path('img/logo_patisserie', views.patte_logo, name='logo_patisserie'),
]