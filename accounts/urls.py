from django.urls import path
from accounts import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('customer/', views.customer, name='customer'),
]