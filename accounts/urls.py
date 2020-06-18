from django.urls import path
from accounts import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),
    path('products/', views.products, name='products'),
    path('customer/<int:id>/', views.customer, name='customer'),
    path('create_order/<str:pk>', views.createOrder, name='create_order'),
    path('update_order/<int:pk>', views.updateOrder, name='update_order'),
    path('delete_order/<int:pk>', views.deleteOrder, name='delete_order'),
]