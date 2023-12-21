from django.shortcuts import render
from store.models import Product
from category.models import Categories

# Create your views here.

def home_page(request):
    products = Product.objects.all().filter(is_available=True)
    category = Categories.objects.all().filter()

    context = {
        'products': products,
        'category': category,
    }

    return render(request, 'product/index.html', context)


   
def AboutUs_page(request):
    return render(request, 'product/about.html')

def blog_page(request):
    return render(request, 'product/blog.html')

def contect_page(request):
    return render(request, 'product/contect.html')

def homep_page(request):
    return render(request, 'product/homep.html')

def cart_page(request):
    return render(request, 'product/cart.html')

def sproduct_page(request):
    return render(request, 'product/sproduct.html')