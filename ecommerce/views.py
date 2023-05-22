from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product, Category, Tag


class Home(ListView):
    model = Product
    template_name = 'ecommerce/index.html'


class DetailProduct(DetailView):
    model = Product
    template_name = 'ecommerce/product_detail.html'


class ListProducts(ListView):
    model = Product
    template_name = 'ecommerce/products_list.html'


def category_products(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    products = category.get_products_by_category()
    return render(request, 'ecommerce/products_list.html', {'object_list': products, 'name_view': category})


def tag_products(request, tag_slug):
    tag = Tag.objects.get(slug=tag_slug)
    products = tag.get_products_by_tag()
    return render(request, 'ecommerce/products_list.html', {'object_list': products, 'name_view': tag})


def on_sales_products(request):
    products = Product.objects.filter(on_sale=True)
    return render(request, 'ecommerce/products_list.html', {'object_list': products, 'name_view': 'Ofertas'})


def order_list(request):
    return render(request, 'ecommerce/order_list.html')


def order_detail(request):
    return render(request, 'ecommerce/order_detail.html')


def error_404(request, exception):
    return render(request, '404.html', status=404)