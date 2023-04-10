from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h4>Проверка работы</h4>")
    # tit = 'Це інший заголовок'
    # return render(request, 'index.html', {'tit': tit})


def main(request):
    return render(request, 'main/index.html')


def catalog(request):
    return render(request, 'main/catalog.html')


def contactUs(request):
    return render(request, 'main/contactUs.html')


def changedContactUs(request, logo):
    if (logo != 'logo') and (logo != 'electro'):
        logo = 'logo'

    return render(request, 'main/contactUs2.html', {'logo': 'main/img/' + logo + '.png'})
