from django import forms
from .models import *
from category.models import *
from django.core.exceptions import ValidationError
class ProductForm(forms.Form):
    title=forms.CharField(max_length=255,required=True)
    category=forms.ChoiceField(choices=Category.get_all_category())
    price=forms.IntegerField(required=True)
    image = forms.CharField(required=True)
    img = forms.ImageField(required=True)
 
 
