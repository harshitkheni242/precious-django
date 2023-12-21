from django.urls import path
from category.views import *

urlpatterns = [
    path('home/', home_page, name='home'),
    path('AboutUs_page/', AboutUs_page, name='AboutUs_page'),
    path('blog_page/', blog_page, name='blog_page'),
    path('contect_page/', contect_page, name='contect_page'),
    path('sproduct_page/', sproduct_page, name='sproduct_page'),
    path('homep_page/', homep_page, name='homep_page'),
    path('cart/', cart_page, name='cart'),
   
]
