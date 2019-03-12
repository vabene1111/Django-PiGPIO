from django.urls import path

from .views import *


urlpatterns = [
    path('', views.index, name='index'),
    path('api/set', SetPinView.as_view(), name='api_set_pin')
]
