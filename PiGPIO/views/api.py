from django.shortcuts import render


def set_pin(request):
    return render(request, 'index.html')
