from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Product, Category, Tag, Order, OrderProduct
from cart.views import clear_cart


PAGINATE_BY = 5

class Home(ListView):
    model = Product
    template_name = 'ecommerce/index.html'


class DetailProduct(DetailView):
    model = Product
    template_name = 'ecommerce/product_detail.html'


class ListProducts(ListView):
    model = Product
    template_name = 'ecommerce/products_list.html'
    paginate_by = PAGINATE_BY

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q', '')
        if query:
            queryset = queryset.filter(Q(name__icontains=query) | Q(category__name__icontains=query))
        orderby = self.request.GET.get('orderby', '')
        if orderby:
            queryset = queryset.order_by(orderby)
        return queryset


def category_products(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    products = category.get_products_by_category()
    paginator = Paginator(products, PAGINATE_BY)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'ecommerce/products_list.html', {
        'object_list': products,
        'name_view': category,
        "page_obj": page_obj}
    )


def tag_products(request, tag_slug):
    tag = Tag.objects.get(slug=tag_slug)
    products = tag.get_products_by_tag()
    paginator = Paginator(products, PAGINATE_BY)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'ecommerce/products_list.html', {
        'object_list': products,
        'name_view': tag,
        "page_obj": page_obj
    })


def on_sales_products(request):
    products = Product.objects.filter(on_sale=True)
    paginator = Paginator(products, PAGINATE_BY)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'ecommerce/products_list.html', {
        'object_list': products,
        'name_view': 'Ofertas',
        "page_obj": page_obj
    })


def order_create(request):
    cart = request.session.get('cart')
    # Check if cart is empty
    if not cart:
        messages.error(request, 'No hay productos en el carrito. Agregá productos para finalizar la compra', extra_tags='warning')
        return redirect('ecommerce:ecommerce')
    # Get products
    cart_products_id = cart.keys()
    products = Product.objects.filter(id__in=cart_products_id)
    '''
    # Check stock
    for product in products:
        amount = cart[str(product.id)]['amount']
        if amount > product.stock:
            messages.error(request, f'La cantidad supera el stock disponible del producto "{product.name[:25]}"', extra_tags='danger')
            return redirect('ecommerce:ecommerce')
    ''' 
    # Create order
    order = Order(user=request.user)
    order.save()
    # Add items
    for product in products:
        amount = cart[str(product.id)]['amount']
        try:
            OrderProduct.objects.create(
                product=product,
                amount=amount,
                order=order,
                price=product.price
            )
            # Subtract stock
            product.stock -= amount
            product.save()
        except Exception as e:
            messages.error(request, str(e), extra_tags='danger')
            order.delete()  # Eliminar el pedido si hay algún error
            return redirect('ecommerce:ecommerce')
    # Clean cart
    clear_cart(request)
    messages.success(request, 'Pedido creado correctamente', extra_tags='success')
    return redirect('ecommerce:order-detail', order.id)


class ListOrder(ListView):
    model = Order
    template_name = 'ecommerce/order_list.html'


class DetailOrder(DetailView):
    model = Order
    template_name = 'ecommerce/order_detail.html'


def error_404(request, exception):
    return render(request, '404.html', status=404)