from django.shortcuts import render,redirect
from . models import Product
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from cart.cart import Cart

@login_required
def index(request):
    item=Product.objects.all()
    return render(request,'index.html',{"item":item})
def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request,'signup.html',{'form':form})
def cart(request):
    item=Product.objects.all()
    return render(request,'cart.html',{"item":item})

@login_required(login_url="/users/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("index")


@login_required(login_url="/users/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart")


@login_required(login_url="/users/login")
def cart_detail(request):
    return render(request, 'cart-details.html')

def contact_us(request):
    item=Product.objects.all()
    return render(request,'contact-us.html',{"item":item})