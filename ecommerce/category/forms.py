from django import forms
from .models import *

class CategoryForm(forms.ModelForm):
    class Meta :
        model = Category
        fields = '__all__'
    # title=forms.CharField(max_length=255,required=True,unique=True)