from django import forms
from .models import product

class productform(forms.ModelForm):

    class Meta:
        model = product
        fields = ['name', 'weight', 'price']
        labels = {'name':'Name', 'weight': 'Weight in grams', 'price': 'Price', }
        widgets = {'name': forms.TextInput(attrs={'class':'form-control'}),
                   'weight': forms.NumberInput(attrs={'class':'form-control'}),
                   'price': forms.NumberInput(attrs={'class':'form-control'}),}