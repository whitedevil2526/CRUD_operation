from django import forms
from .models import Shoes  # Make sure 'Shoes' is correctly imported

class ShoeForm(forms.ModelForm):
    class Meta:
        model = Shoes  # Ensure it's capitalized correctly
        fields = ['name', 'genre', 'prize', 'desc', 'image']
