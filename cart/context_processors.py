def get_cart_total(request):
    sum = 0
    for key, value in request.session["cart"].items():
        sum += float(value['sum'])
    return {'get_cart_total': sum}