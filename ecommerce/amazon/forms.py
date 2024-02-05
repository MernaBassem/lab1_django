from django import forms
from .models import *
from django.core.exceptions import ValidationError
class ProductForm(forms.Form):
    title=forms.CharField(max_length=255,required=True)
    category=forms.CharField(max_length=255,required=True)
    price=forms.IntegerField(required=True)
    image = forms.CharField(required=True)
    img = forms.ImageField(required=True)
 
 
# def clean_name(self):
#     user_name=self.cleaned_data['title']
#     obj=Product.objects.get(title=user_name).exsists()
    
#     if(obj):
#         raise ValidationError("must be unique")
#     else:
#         return True
    
