from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'ecommerce/index.html')


def compra(request):
    context = {'precio': '99.000',
               'nombre': 'Samsung Galaxy A04 128 GB negro 4 GB RAM',
               'detalle': "Some quick example text to build on the card title and make up the bulk of the card's content. Some quick example text to build on the card title and make up the bulk of the card's content.",
               'cuotas': 'en 6x de $ 16.500',
               }
    return render(request, 'ecommerce/compra.html', context)


