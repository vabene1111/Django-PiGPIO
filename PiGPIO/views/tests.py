from django.shortcuts import render


def blockly_custom(request):
    return render(request, 'tests/blockly_custom.html', {})
