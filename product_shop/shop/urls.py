from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.home, name='home'),
    path('item/', views.item, name='item'),
    path('catalog/', views.product_list, name='catalog'),
    path('catalog/<slug:category_slug>/',
         views.product_list, name='category_detail'),
    path('catalog/<slug:category_slug>/<slug:product_slug>/',
         views.product_detail, name='product_detail'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
]
