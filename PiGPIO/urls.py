from django.urls import path

from .views import *


urlpatterns = [
    path('', views.index, name='index'),

]
