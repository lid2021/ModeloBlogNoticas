from django.shortcuts import render


def base(request):
    return render(request, 'base.html')

def Index(request):
    return render(request, 'index.html')

def nosotros(request):
    return render(request, 'nosotros.html')
