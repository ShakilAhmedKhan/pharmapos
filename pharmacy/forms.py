from django import forms
from .models import Customer, Medicine, Sale, SaleItem
from django.forms import inlineformset_factory

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = '__all__'

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['customer']

class SaleItemForm(forms.ModelForm):
    class Meta:
        model = SaleItem
        fields = ['medicine', 'quantity']

SaleItemFormSet = inlineformset_factory(Sale, SaleItem, form=SaleItemForm, extra=3)