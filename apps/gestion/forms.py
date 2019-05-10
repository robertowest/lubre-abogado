from datetime import datetime
from django import forms

from apps.gestion.models import accion as models

class AccionForm(forms.ModelForm):
    fecha = forms.DateField(initial=datetime.now())
    idenc_mov = forms.IntegerField(widget=forms.HiddenInput())

    class Meta:
        model = models.Accion
        fields = ['fecha', 'tipo', 'observacion', 'idenc_mov']