from django import forms
from .models import Shoes

class ShoeForm(forms.ModelForm):
    class Meta:
        model = Shoes
        fields = ['name', 'brand', 'price', 'desc','image']  # Use correct field names
