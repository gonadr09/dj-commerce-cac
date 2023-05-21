from django.shortcuts import render, redirect, get_object_or_404
from ecommerce.models import Product


def get_cart(request):
    cart = request.session.get('cart')
    if not cart:
        cart = request.session['cart'] = {}
    return cart


def add_to_cart(request, product_id):
    cart = get_cart(request)
    product = get_object_or_404(Product, id=product_id)
    product_id = str(product_id)
    if str(product_id) not in cart:
        cart[product_id] = {
            'name': product.name,
            'image': product.get_main_image().image.url,
            'price': str(product.price),
            'amount': 1,
            'sum': str(product.price),
        }
    else:
        cart[product_id]['amount'] += 1
        cart[product_id]['sum'] = '{:.2f}'.format(float(cart[product_id]['sum']) + float(cart[product_id]['price']))
    request.session.modified = True
    return redirect('ecommerce:home')


def subtract_from_cart(request, product_id):
    cart = get_cart(request)
    product_id = str(product_id)
    if product_id in cart:
        if cart[product_id]['amount'] > 1:
            cart[product_id]['amount'] -= 1
            cart[product_id]['sum'] = '{:.2f}'.format(float(cart[product_id]['sum']) - float(cart[product_id]['price']))
        else:
            del cart[product_id]
    request.session.modified = True
    return redirect('ecommerce:home')


def remove_from_cart(request, product_id):
    pass


def clear_cart(request):
    pass