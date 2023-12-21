from django.db import models
from base.models import BaseModel
from category.models import Categories
from django.urls import reverse

# Create your models here.

class Product(BaseModel):
    product_name    = models.CharField(max_length=200, unique=True)
    slug            = models.SlugField(max_length=200, unique=True)
    description     = models.TextField(max_length=200, blank=True)
    price           = models.IntegerField()
    image           = models.ImageField(upload_to='photos/products')
    stock           = models.IntegerField()
    is_available    = models.BooleanField(default=True)
    category        = models.ForeignKey(Categories, on_delete=models.CASCADE)
    created_date    = models.DateTimeField(auto_now_add=True)
    modified_date   = models.DateTimeField(auto_now=True)
    
    def get_url(self):
        return reverse('product_details', args=[self.category.slug, self.slug]) 
    
    def __sef__(self):
        return self.product_name
