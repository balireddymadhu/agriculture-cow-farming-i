from django.shortcuts import render


def hellow(request):
    return render(request, 'home.html')
