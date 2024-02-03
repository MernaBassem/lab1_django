from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=50)
    category = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    image = models.CharField(max_length=150)
    active = models.BooleanField(default=True)
    
    
    def __str__(self) :
        return self.title
