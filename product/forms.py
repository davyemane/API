from .models import Product
from django import forms

class ProductForms(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'content', 'price')
