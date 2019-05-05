from django import forms

from .models import ClientesSucursal, Clientes, Vendedores


class PruebaForm(forms.Form):
    vendedor = forms.ModelChoiceField(label=u'Vendedor', queryset=Vendedores.objects.all())
    cliente = forms.ModelChoiceField(label=u'Cliente', queryset=Clientes.objects.all())


    def __init__(self, *args, **kwargs):
        super(PruebaForm, self).__init__(*args, **kwargs)
        self.fields['vendedor'].queryset = Vendedores.objects.using('firebird').all()
        #self.fields['cliente'].queryset = Clientes.objects.none()
        self.fields['cliente'].queryset = Clientes.objects.using('firebird').filter(idcliente=9893)
