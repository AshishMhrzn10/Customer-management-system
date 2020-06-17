from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Customer, Product, Order, Tag
from .forms import OrderForm
from .filters import OrderFilter
from django.forms import inlineformset_factory

# Create your views here.
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    context = {'orders':orders, 'customers':customers, 'total_customers':total_customers, 'total_orders':total_orders, 'delivered':delivered, 'pending':pending}
    return render(request,'home.html', context)

def products(request):
    products = Product.objects.all()
    return render(request,'products.html',{'products':products})

def customer(request,id):
    customer = Customer.objects.get(id=id)

    orders = customer.order_set.all()
    order_count = orders.count()

    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs
    context={'customer':customer, 'orders':orders, 'order_count':order_count, 'myFilter':myFilter}
    return render(request,'customer.html',context)


def createOrder(request, pk):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product','status'), extra=5)
    customer = Customer.objects.get(id=pk)
    formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)
    #form = OrderForm(initial={'customer':customer})
    if request.method == "POST":
        #form = OrderForm(request.POST)
        formset = OrderFormSet(request.POST,instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect("/")

    context={'formset':formset}
    return render(request,'order_form.html',context)


def updateOrder(request,pk):
    order = Order.objects.get(id=pk)
    form=OrderForm(instance=order) 
    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect("/")
    context={'form':form}
    return render(request,'order_form.html',context)


def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect("/")

    context={'item':order}
    return render(request,'delete.html',context)