from django.contrib.auth import authenticate, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import UserForm
from .models import Product, Basket, Customer, BasketProducts, CustomerDetails, Order, OrderProducts


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
    count = request.POST["productCount"]
    product = Product.objects.get(title=title)
    if 'username' in request.session:
        username = request.session['username']
        user = Customer.objects.get(username=username)
        if Basket.objects.filter(user=user).exists():
            basket = Basket.objects.get(user=user)
        else:
            basket = Basket()
            basket.customer = user
            basket.id = 0
            basket.save()
        if BasketProducts.objects.filter(product=product).exists():
            basketProducts = BasketProducts.objects.get(product=product)
            basketProducts.countOfProducts = basketProducts.countOfProducts + int(count)
            basketProducts.save()
        else:
            basketProducts = BasketProducts()
            basketProducts.basket = basket
            basketProducts.product = product
            basketProducts.countOfProducts = count
            basketProducts.save()
        return redirect('catalog')
    else:
        return redirect('login')


def getBasket(request):
    if 'username' in request.session:
        username = request.session['username']
        user = Customer.objects.get(username=username)
        basket = Basket.objects.filter(user=user).first()
        basketProducts = BasketProducts.objects.filter(basket=basket)
        totalSum = 0
        for basketProduct in basketProducts:
            totalSum += int(basketProduct.product.price) * int(basketProduct.countOfProducts)
        return render(request, 'main/basket.html', {'basketProducts': basketProducts, 'totalSum': totalSum})
    else:
        return redirect('login')


def deleteProductFromBasket(request, title):
    product = Product.objects.get(title=title)
    BasketProducts.objects.filter(product=product).delete()
    return getBasket(request)


def deleteBasket(request):
    if 'username' in request.session:
        username = request.session['username']
        user = Customer.objects.get(username=username)
        basket = Basket.objects.filter(user=user).first()
        BasketProducts.objects.filter(basket=basket).delete()
    return getBasket(request)


def createOrderPage(request):
    global userDetails
    if 'username' in request.session:
        username = request.session['username']
        user = Customer.objects.get(username=username)
        basket = Basket.objects.filter(user=user).first()
        basketProducts = BasketProducts.objects.filter(basket=basket)
        totalSum = 0
        for basketProduct in basketProducts:
            totalSum += int(basketProduct.product.price) * int(basketProduct.countOfProducts)

        if CustomerDetails.objects.filter(user=user).exists():
            userDetails = CustomerDetails.objects.get(user=user)
        print(user.username)
        return render(request, 'main/order.html', {'userDetails': userDetails, 'totalSum': totalSum})
    else:
        return redirect('login')


def createOrder(request):
    if 'username' in request.session:
        username = request.session['username']
        user = Customer.objects.get(username=username)
        basket = Basket.objects.filter(user=user).first()
        basketProducts = BasketProducts.objects.filter(basket=basket)
        CustomerDetails.objects.get(user=user)
        order = Order()
        previousOrder = Order.objects.all().last()
        order.id = previousOrder.id + 1
        order.customer = user
        order.status = 'in process'
        order.save()
        for basketProduct in basketProducts:
            orderProducts = OrderProducts()
            orderProducts.order = order
            orderProducts.product = basketProduct.product
            orderProducts.countOfProducts = basketProduct.countOfProducts
            orderProducts.save()
        BasketProducts.objects.filter(basket=basket).delete()
        return render(request, 'main/success.html')
    else:
        return redirect('login')
