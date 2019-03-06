from django.urls import path

from .views import *


urlpatterns = [
    path('', views.index, name='index'),
    path('api/set', api.set_pin, name='api_set_pin')
]
