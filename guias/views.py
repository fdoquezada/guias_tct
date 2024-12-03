from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import GuiaCombustible
from .forms import GuiaCombustibleForm

def home(request):
    return render(request, 'guias/home.html')

@login_required
def crear_guia(request):
    if request.method == 'POST':
        form = GuiaCombustibleForm(request.POST, request.FILES)
        if form.is_valid():
            guia = form.save(commit=False)
            guia.usuario = request.user
            guia.save()
            return redirect('listar_guias')
    else:
        form = GuiaCombustibleForm()
    return render(request, 'guias/crear_guia.html', {'form': form})

@login_required
def listar_guias(request):
    guias = GuiaCombustible.objects.filter(usuario=request.user)
    return render(request, 'guias/listar_guias.html', {'guias': guias})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    return render(request, 'registration/logout.html')