from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, logout
from .forms import RegistrationForm,Product
from .models import Product , BasketItem, Order

def Welcome(request):
    return render(request, 'webapp/welcome.html')

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'webapp/register.html', {'form': form})

def product(request):
    products = Product.objects.all()
    return render(request, 'webapp/product.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'webapp/product_detail.html', {'product': product})


def add_to_basket(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
    else:
        quantity = 1

    try:
        item = BasketItem.objects.get(user=request.user, product=product)
        item.quantity = item.quantity + quantity
        item.save()
    except BasketItem.DoesNotExist:
        item = BasketItem(user=request.user, product=product, quantity=quantity)
        item.save()

    messages.success(request, 'Product added to your basket.')

    return redirect('product')


def basket(request):
    items = BasketItem.objects.filter(user=request.user)

    if request.method == 'POST':
        if 'clear' in request.POST:
            items.delete()
            return redirect('basket')

        for item in items:
            field_name = 'quantity_%d' % item.id
            if field_name in request.POST:
                new_q = int(request.POST[field_name])
                if new_q <= 0:
                    item.delete()
                else:
                    item.quantity = new_q
                    item.save()

        return redirect('basket')

    total = 0
    for item in items:
        total = total + item.line_total()

    context = {'items': items, 'total': total}
    return render(request, 'webapp/basket.html', context)

def logout_user(request):
    logout(request)
    return redirect('login')

def order_page(request):
    items = BasketItem.objects.filter(user=request.user)
    basket_items = []
    total = 0

    for item in items:
        subtotal = item.product.price * item.quantity
        total += subtotal

        basket_items.append({'product': item.product, 'quantity': item.quantity, 'price': item.product.price,
                            'subtotal': subtotal
        })

    context = {'basket_items': basket_items,'total': total
    }

    if request.method == "POST":
        if not basket_items:
            return redirect('basket')

        new_order = Order.objects.create(
            user=request.user,
            total=total
        )   

        items.delete()
        return redirect('product')

    context = {'basket_items': basket_items,'total': total}
    return render(request, 'webapp/order.html', context)


