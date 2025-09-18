from django import forms
from .models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class WebContentForm(forms.ModelForm):
    class Meta:
        model = WebContent
        fields = '__all__'

class shopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = '__all__'