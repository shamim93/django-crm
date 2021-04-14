from django.urls import path
from .import views

app_name='accounts'

urlpatterns=[
    path('',views.home,name='home'),
    path('product',views.product,name='product'),
    path('customer/create',views.createcustomer,name='createcustomer'),
    path('order/create',views.createOrder,name='createorder'),
    path('order/edit/<int:order_id>/',views.editOrder,name='editorder'),
    path('customer/<int:customer_id>',views.customer,name='customer'),
]