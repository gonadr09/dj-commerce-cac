from .views import get_cart 


def get_cart_total(request):
    cart = get_cart(request)
    cart_total = 0
    for key, value in cart.items():
        cart_total += float(value['sum'])
    return {'get_cart_total': cart_total}