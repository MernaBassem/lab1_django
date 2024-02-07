from django.db import models
from category.models import Category

class Product(models.Model):
    title = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.CharField(max_length=150)
    img = models.ImageField(upload_to='amazon/images/', blank=True, null=False, default='')

    @classmethod
    def get_product_detail(cls, id):
        return cls.objects.get(id=id)