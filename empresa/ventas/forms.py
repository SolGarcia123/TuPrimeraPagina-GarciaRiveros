from django import forms
from .models import Proveedor, Cliente, Baldosa

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = '__all__'

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class BaldosaForm(forms.ModelForm):
    class Meta:
        model = Baldosa
        fields = '__all__'