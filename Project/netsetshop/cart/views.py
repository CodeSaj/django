from django.shortcuts import render, get_object_or_404
from onlineshop.models import Product
from .cart import Cart
from django.views.decorators.http import require_POST
from .forms import *


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CardAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        card.add(product=product, quantity=cd['quantity'], override_quantity=cd['override'])
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request, product_id):
    cart = Cart(request)
    context = {
        'cart':cart,
    }
    return render(request, 'cart/detail.html', context)