from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('data', views.store_data, name='store_data'),
    path('index', views.index, name='index'),
    path('img/icon_cafe', views.cafe_img, name='icon_cafe'),
    path('img/icon_patisserie', views.patte_img, name='icon_patisserie'),
    path('img/logo_cafe', views.cafe_logo, name='logo_cafe'),
    path('img/logo_patisserie', views.patte_logo, name='logo_patisserie'),
]