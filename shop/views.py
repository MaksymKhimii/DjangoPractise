from django.contrib.auth import authenticate, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import UserForm
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
    logo = 'logo'
    return render(request, 'main/contactUs.html', {'logo': 'main/img/' + logo + '.png'})


def changedContactUs(request, logo):
    if (logo != 'logo') and (logo != 'electro'):
        logo = 'logo'

    return render(request, 'main/contactUs.html', {'logo': 'main/img/' + logo + '.png'})


def loginPage(request):
    form = UserForm()
    data = {
        'form': form
    }
    return render(request, 'main/login.html', data)


def loginAction(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    request.session['username'] = username
    if user is not None:
        return redirect('catalog')
    else:
        return redirect('login')


def logoutAction(request):
    logout(request)
    return redirect('main')


def addToBasket(request):
    title = request.POST["title"]
    price = request.POST["price"]
    count = request.POST["productCount"]

    print('title: ' + title + 'price: ' + price + 'count: ' + count)
    return redirect('catalog')
