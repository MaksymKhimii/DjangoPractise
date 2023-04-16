from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('main', views.main, name='main'),
    path('catalog', views.catalog, name='catalog'),
    path('contactUs', views.contactUs, name='contactUs'),
    path('contactUs/<str:logo>', views.changedContactUs, name='contactUs'),
    path('login', views.loginPage, name='login'),
    path('check-user', views.loginAction, name ='check-user'),
    path('logout', views.logoutAction, name='logout'),
    path('addToBasket', views.addToBasket, name='addToBasket'),
    path('basket', views.getBasket, name='basket')
    # добавляем все страницы + контроллер который возращает
    # хтмл + имя, которе потом указываем с помощью джинджа в ссылке для перехода
]
