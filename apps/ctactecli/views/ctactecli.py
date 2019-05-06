from django.shortcuts import render
from datetime import datetime

from apps.ctactecli import models


def index(request):
    context = {}
    data = models.CtaCteCliResu.search(1, datetime.now(), 0)
    context = {'dataset': data}
    return render(request, 'ctactecliresu/index.html', context)


def cargar_vendedores_ajax(request):
    data = models.Vendedores.objects.using('firebird').all().order_by('nombre')
    context = {'vendedores': data}
    return render(request, 'ctactecliresu/include/cargar_vendedores.html', context)


def cargar_clientes_ajax(request):
    vendedorId = request.GET['uf']
    data = models.ClientesSucursal.objects.using('firebird').all().\
        filter(vendedores_id=vendedorId).select_related('clientes').order_by('clientes__nombre')
    context = {'clientes': data}
    return render(request, 'ctactecliresu/include/cargar_clientes.html', context)


def cargar_resultado_ajax(request):
    clienteId = request.GET['uf']
    data = models.CtaCteCliResu.search(clienteId, datetime.now(), 0)
    context = {'dataset': data}
    return render(request, 'ctactecliresu/include/cargar_resultado.html', context)


def info(request, filter):
    from django.urls import reverse
    return reverse('accion:deuda/'+str(filter))


"""
# from django.apps import apps

from mainapp.models import mainappmodel
def currentappview(request):
    all = mainappmodel.objects.all()
    return render(request, "pages/home.html", {'all': all})
"""