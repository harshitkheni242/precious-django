# urls.py
from django.urls import path
from store.views import *

urlpatterns = [
    path('shop_page/', shop_page, name='shop_page'),
    path('<slug:category_slug>/', shop_page, name='products_by_category'),
    path('<slug:category_slug>/<slug:product_slug>/', product_details, name='product_details'),
]
