from django import forms
from .models import GuiaCombustible

class GuiaCombustibleForm(forms.ModelForm):
    class Meta:
        model = GuiaCombustible
        fields = ['titulo', 'periodo', 'fecha', 'nombre_conductor', 'fecha_carga', 'guia', 'patente', 'estacion_servicio', 'suministro', 'kms', 'consumo', 'imagen']