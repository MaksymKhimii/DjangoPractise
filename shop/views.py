from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
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
    # ajax version of catalog loading
    return render(request, 'main/catalog-with-ajax.html', {'products': products})
    # basic render response
    # return render(request, 'main/catalog.html', {'products': products})


def getAllProducts(request):
    products = Product.objects.all()
    return JsonResponse(list(products.values()), safe=False)


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
    if user is not None:
        login(request, user)
        request.session['username'] = username
        return redirect('catalog')
    else:
        return redirect('login')


def logoutAction(request):
    logout(request)
    return redirect('main')


@login_required(login_url='login')
def addToBasket(request):
    title = request.POST["title"]
    count = request.POST["productCount"]
    product = Product.objects.get(title=title)
    if 'username' in request.session:
        username = request.user.username
        user = Customer.objects.get(username=username)
        if Basket.objects.filter(customer=user).exists():
            basket = Basket.objects.get(customer=user)
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


@login_required(login_url='login')
def getBasket(request):
    if request.user.is_authenticated and request.user.username != '':
        username = request.user.username
        user = Customer.objects.get(username=username)
        basket = Basket.objects.filter(customer=user).first()
        basketProducts = BasketProducts.objects.filter(basket=basket)
        totalSum = 0
        for basketProduct in basketProducts:
            totalSum += int(basketProduct.product.price) * int(basketProduct.countOfProducts)
        return render(request, 'main/basket.html', {'basketProducts': basketProducts, 'totalSum': totalSum})
    else:
        return redirect('login')


@login_required(login_url='login')
def deleteProductFromBasket(request, title):
    product = Product.objects.get(title=title)
    BasketProducts.objects.filter(product=product).delete()
    return getBasket(request)


@login_required(login_url='login')
def deleteBasket(request):
    if request.user.is_authenticated and request.user.username != '':
        username = request.user.username
        user = Customer.objects.get(username=username)
        basket = Basket.objects.filter(customer=user).first()
        BasketProducts.objects.filter(basket=basket).delete()
    return getBasket(request)


@login_required(login_url='login')
def createOrderPage(request):
    global userDetails
    if request.user.is_authenticated and request.user.username != '':
        username = request.user.username
        user = Customer.objects.get(username=username)
        basket = Basket.objects.filter(customer=user).first()
        basketProducts = BasketProducts.objects.filter(basket=basket)
        totalSum = 0
        for basketProduct in basketProducts:
            totalSum += int(basketProduct.product.price) * int(basketProduct.countOfProducts)

        if CustomerDetails.objects.filter(customer=user).exists():
            userDetails = CustomerDetails.objects.get(customer=user)
        print(user.username)
        return render(request, 'main/order.html', {'userDetails': userDetails, 'totalSum': totalSum})
    else:
        return redirect('login')


@login_required(login_url='login')
def createOrder(request):
    if request.user.is_authenticated and request.user.username != '':
        username = request.user.username
        user = Customer.objects.get(username=username)
        basket = Basket.objects.filter(customer=user).first()
        basketProducts = BasketProducts.objects.filter(basket=basket)
        CustomerDetails.objects.get(customer=user)
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


@login_required(login_url='login')
def getAllCustomerOrders(request):
    if request.user.is_authenticated and request.user.username != '':
        username = request.user.username
        user = Customer.objects.get(username=username)
        orders = Order.objects.filter(customer=user)
        return render(request, 'main/orders.html', {'orders': orders})
    else:
        return redirect('login')


@login_required(login_url='login')
def getOrderById(request, id):
    if request.user.is_authenticated:
        order = Order.objects.filter(id=id).first()
        orderProducts = OrderProducts.objects.filter(order=order)
        totalSum = 0
        for orderProduct in orderProducts:
            totalSum += int(orderProduct.product.price) * int(orderProduct.countOfProducts)
        return render(request, 'main/orderById.html', {'order': order,
                                                       'id': id,
                                                       'orderProducts': orderProducts,
                                                       'totalSum': totalSum})
    else:
        return redirect('login')
