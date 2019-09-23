from django.shortcuts import render, get_object_or_404
from webapp.models import Product


def index_view(request):
    products = Product.objects.filter(amount__gt=0).order_by('category', 'name')
    return render(request, 'index.html', context={
        'products': products
    })


def product_detail_view(request, pk):
    product = get_object_or_404(Product, pk=pk)

    return render(request, 'product.html', context={
        'product': product
    })


def search_view(request):
    search = request.GET.get('search', '')
    products = Product.objects.filter(name__contains=search)
    return render(request, 'index.html', context={'products': products})