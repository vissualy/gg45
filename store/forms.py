from django import forms
from .models import Product,Category
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            "category",
            "tittle",
            "banner",
            "video",
            'description',
            "price",)
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ("tittle",)