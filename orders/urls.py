"""
URL configuration for orders project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter

from diplom.views import LoginAccount, RegisterAccount, PartnerUpdate, PartnerState, PartnerUpdate, PartnerOrders, ConfirmAccount, AccountDetails, \
    BasketView, CategoryView, ShopView, ContactView,  ProductInfoView, ProductInfoView, OrderView

from django_rest_passwordreset.views import reset_password_request_token, reset_password_confirm

r = DefaultRouter()

r.register('input', LoginAccount)
r.register('register', RegisterAccount)
r.register('partner (update)', PartnerUpdate)
r.register('partner (state)', PartnerState)
r.register('partner (orders)', PartnerOrders)
r.register('confirm', ConfirmAccount)
r.register('details', AccountDetails)

r.register('basket', BasketView)
r.register('categories', CategoryView)
r.register('shops', ShopView)
r.register('contact', ContactView)
r.register('products', ProductInfoView)
r.register('order', OrderView)

r.register('password (reset)', reset_password_request_token)
r.register('password (confirm)', reset_password_confirm)

urlpatterns = [
    path('admin/', admin.site.urls),
] + r.urls

