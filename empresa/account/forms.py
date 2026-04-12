from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class RegistroForm(UserCreationForm):
    email = forms.EmailField()
    nombre = forms.CharField()
    apellido = forms.CharField()
    fecha_nacimiento = forms.DateField()
    dni = forms.IntegerField()
    imagen = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = [
            'username', 'email',
            'nombre', 'apellido',
            'fecha_nacimiento', 'dni', 'imagen',
            'password1', 'password2'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].help_text = None
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None

        self.fields['username'].label = "Usuario"
        self.fields['password1'].label = "Contraseña"
        self.fields['password2'].label = "Repetir contraseña"

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['nombre', 'apellido', 'fecha_nacimiento', 'dni', 'imagen']