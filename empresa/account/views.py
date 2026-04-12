from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm, ProfileForm
from .models import Profile

def register_view(request):
    mensaje_exito = None
    mensaje_error = None

    if request.method == "POST":
        form = RegistroForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()

            Profile.objects.create(
                user=user,
                nombre=form.cleaned_data['nombre'],
                apellido=form.cleaned_data['apellido'],
                fecha_nacimiento=form.cleaned_data['fecha_nacimiento'],
                dni=form.cleaned_data['dni'],
                imagen=form.cleaned_data.get('imagen')
            )

            mensaje_exito = "Usted se ha registrado correctamente."
            form = RegistroForm()
        else:
            mensaje_error = "La contraseña no cumple con las condiciones."

    else:
        form = RegistroForm()

    return render(request, 'account/register.html', {
        'form': form,
        'mensaje_exito': mensaje_exito,
        'mensaje_error': mensaje_error
    })


def login_view(request):
    error = None

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
        else:
            error = "Nombre de usuario o contraseña inválidos."

    else:
        form = AuthenticationForm()

    return render(request, 'account/login.html', {'form': form, 'error': error})


def logout_view(request):
    logout(request)
    return redirect('/account/login/')


@login_required
def editar_perfil(request):
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)

        if request.POST.get("eliminar_imagen"):
            profile.imagen.delete(save=False)
            profile.imagen = None

        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'account/editar_perfil.html', {'form': form})