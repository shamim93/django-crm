from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product,Customer,Order
from django.db.models import Sum
from .forms import CustomerForm,OrderForm
def home(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()
    total_orders = orders.count()
    order_delivered = orders.filter(status='delivered').count()
    order_pending = orders.filter(status='pending').count()
    context = {
        'customers': customers,
        'orders': orders,
        'total_orders': total_orders,
        'order_delivered' : order_delivered,
        'order_pending': order_pending
    }
    return render(request,"accounts/dashboard.html",context)

def product(request):
    products = Product.objects.all()
    total_price =  sum(products.values_list('price', flat=True))
    context ={
        'products': products,
        'total_price':total_price
    }
    return render(request,"accounts/products.html",context)

def customer(request,customer_id):
    customer = get_object_or_404(Customer,pk=customer_id)
    
    # total_orders = customer
    orders = customer.order_set.all()
    total_orders = orders.count()
    return render(request,"accounts/customer.html",{'customer':customer,'orders':orders,'total_orders':total_orders})

# customer creation
@login_required
def createcustomer(request):
    if request.method == "GET":
        return render(request,"accounts/createcustomer.html",{'customerform': CustomerForm})
    else:
        try:
            formdata = CustomerForm(request.POST)
            # newdata = formdata.save(commit=False)
            # newdata.user = request.user
            # newdata.save()
            if formdata.is_valid():
                formdata.save()
                return redirect('accounts:home')
        except ValueError:
            return render(request,"accounts/createcustomer.html",{'customerform': CustomerForm,'error': 'Seems email and phone already exists! Please try new one.'})
# order creation
@login_required
def createOrder(request):
    if request.method == "POST":
        formdata = OrderForm(request.POST)
        formdata.save()
        return redirect('accounts:home')
    else:
        return render(request,'accounts/createorder.html',{'orderform': OrderForm})

# edit order
def editOrder(request,order_id):
    order = get_object_or_404(Order,pk=order_id)
    if request.method == "POST":
        formdata = OrderForm(request.POST,instance=order)
        formdata.save()
        return redirect('accounts:home')
    else:
        formdata = OrderForm(instance=order)
        return render(request,'accounts/editorder.html',{'formdata':formdata,'orderform':OrderForm})