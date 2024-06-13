from django.shortcuts import render

def home(request):
  return render(request, 'shop/index.html')

def item(request):
  return render(request, 'item.html')

def product_list(request, category_slug=None):
  return render(request, 'shop/catalog.html')

def product_detail(request, category_slug, product_slug):
  return render(request, 'shop/product_detail.html')

def cart(request):
  return render(request, 'shop/cart.html')

def checkout(request):
  return render(request, 'shop/checkout.html') 
