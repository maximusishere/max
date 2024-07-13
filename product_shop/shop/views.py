from django.shortcuts import render
from .models import Product, Category


def home(request):
    products = Product.objects.all()[:9]
    return render(request, 'shop/index.html', {'products': products})


def item(request):
    return render(request, 'item.html')


def product_list(request, category_slug=None):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})


def product_detail(request, category_slug, product_slug):
    return render(request, 'shop/product_detail.html')


def cart(request):
    return render(request, 'shop/cart.html')


def checkout(request):
    return render(request, 'shop/checkout.html') 
