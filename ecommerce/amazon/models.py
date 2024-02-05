from django.db import models

from category.models import *

class Product(models.Model):
    title = models.CharField(max_length=50, default='Default Title')
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.CharField(max_length=150, default='https://cdn.dummyjson.com/product-images/24/thumbnail.jpg')
    img = models.ImageField(upload_to='amazon/images/', blank=True, null=False ,default='')
    active = models.BooleanField(default=True)


    
    
