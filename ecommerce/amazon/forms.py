from django import forms
from .models import *
from category.models import *
class ProductForm(forms.ModelForm):
    class Meta :
        model = Product
        fields = '__all__'
    # title=forms.CharField(max_length=255,required=True)
    # category=forms.ChoiceField(choices=Category.get_all_category())
    # price=forms.IntegerField(required=True)
    # image = forms.CharField(required=True)
    # img = forms.ImageField(required=True)



