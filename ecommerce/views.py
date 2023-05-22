from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product, Category, Tag


products = [
    {
        'id': 1,
        'title': 'Xiaomi Redmi Note 11 (Snapdragon) Dual SIM 128 GB azul estelar 4 GB RAM',
        'detail': "Dispositivo liberado para que elijas la compañía telefónica que prefieras. Pantalla AMOLED de 6.43. Tiene 4 cámaras traseras de 50Mpx / 8Mpx / 2Mpx / 2Mpx. Cámara delantera de 13Mpx. Procesador Snapdragon 680 Octa-Core de 2.4GHz con 4GB de RAM. Batería de 5000mAh. Memoria interna de 128GB. Con reconocimiento facial y sensor de huella dactilar. Resistente al polvo.",
        'category': 'Smartphones',
        'price': '100.999',
        'installments': 'en 9x de $ 11.222',
        'images': ['img/product1-1.jpg', 'img/product1-2.jpg', 'img/product1-3.jpg']
    },
    {
        'id': 2,
        'title': 'Notebook Lenovo Ideapad I7 1165g7 8gb 512gb Pantalla 14 Full Hd Windows 11 Home',
        'detail': "Procesador Intel Core i7. Memoria RAM de 8GB. La duración de la batería depende del uso que se le dé al producto.",
        'category': 'Computación',
        'price': '362.999',
        'installments': 'en 9x de $ 40.333',
        'images': ['img/product2-1.jpg', 'img/product2-2.jpg', 'img/product2-3.jpg']
    },
    {
        'id': 3,
        'title': 'Silla de escritorio Xtrike Me GC-905 gamer ergonómica azul y negro con tapizado de cuero sintético',
        'detail': "Confortable y duradera. Posee altura ajustable. Cómodos apoyabrazos. Soporte lumbar regulable. Tiene apoya cabeza. Con ruedas. Giratoria. Peso máximo soportado: 135 kg. Medidas del asiento: 53 cm de ancho, 44 cm de altura mínima desde el piso, 54 cm de altura máxima desde el piso y 50 cm de profundidad. Medidas del respaldo: 57 cm de ancho y 85 cm de alto. La silla alcanza una altura mínima de 125 cm y máxima de 135 cm.",
        'category': 'Escritorios y sillas',
        'price': '62.853',
        'installments': 'en 9x de $ 6.983',
        'images': ['img/product3-1.jpg', 'img/product3-2.jpg', 'img/product3-3.jpg']
    },
    {
        'id': 4,
        'title': 'Microsoft Xbox Series X 1TB Standard color negro con joystick inalámbrico',
        'detail': "Incluye control. Resolución de 2560px x 1440px. Memoria RAM de 16GB. Cuenta con: 1 cable hdmi, 1 cable de alimentación ca. La duración de la batería de los controles depende del uso que se le dé al producto.",
        'category': 'Consolas y videojuegos',
        'price': '359.999',
        'installments': 'en 9x de $ 39.999',
        'images': ['img/product4-1.jpg', 'img/product4-2.jpg', 'img/product4-3.jpg']
    },
    {
        'id': 5,
        'title': 'Monitor Gamer Samsung F24t35 Led 24 Full Hd Full HD Widescreen 16:9',
        'detail': "Alto 42.5. Ancho 53.9. Color NEGRO. Modelo LF24T350FH. Origen ARGENTINA. Peso 2.7. Profundidad 23.2. Brillo 250 CD/M2. Formato de pantalla WIDESCREEN 16:9. Frecuencia Vert. 60. Radio de contraste 1000 A 1. Tiempo de respuesta 5",
        'category': 'Computación',
        'price': '57.799',
        'installments': 'en 12x de $ 7.087',
        'images': ['img/product5-1.jpg', 'img/product5-2.jpg', 'img/product5-3.jpg']
    },
]

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