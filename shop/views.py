from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


def index(request):
    return HttpResponse("<h4>Проверка работы</h4>")
    # tit = 'Це інший заголовок'
    # return render(request, 'index.html', {'tit': tit})


def main(request):
    return render(request, 'main/index.html')


def catalog(request):
    products = Product.objects.all()
    return render(request, 'main/catalog.html', {'products': products})


def contactUs(request):
    return render(request, 'main/contactUs.html')


def changedContactUs(request, logo):
    if (logo != 'logo') and (logo != 'electro'):
        logo = 'logo'

    return render(request, 'main/contactUs2.html', {'logo': 'main/img/' + logo + '.png'})


def loginPage(request):
    return render(request, 'main/login.html')
