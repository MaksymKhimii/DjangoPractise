from django.contrib.auth.views import LoginView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('main', views.main, name='main'),
    path('catalog', views.catalog, name='catalog'),
    path('contactUs', views.contactUs, name='contactUs'),
    path('contactUs/<str:logo>', views.changedContactUs, name='contactUs'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('check-user', views.loginAction, name='check-user'),
    path('accounts/logout/', views.logoutAction, name='logout'),
    path('addToBasket', views.addToBasket, name='addToBasket'),
    path('basket', views.getBasket, name='basket'),
    path('deleteProductFromBasket/<str:title>', views.deleteProductFromBasket, name='deleteProductFromBasket'),
    path('deleteBasket', views.deleteBasket, name='deleteBasket'),
    path('orderPage', views.createOrderPage, name='orderPage'),
    path('createOrder', views.createOrder, name='createOrder'),
    path('orders', views.getAllCustomerOrders, name='orders'),
    path('orders/<int:id>', views.getOrderById, name='order'),
    path('getAllProducts', views.getAllProducts, name='getAllProducts')
]
