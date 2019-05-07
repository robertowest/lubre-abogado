from datetime import datetime

from django.shortcuts import render

from apps.gestion import models

def index(request):
    context = {}
    # data = models.DeudaView.objects.filter(cliente=1059)
    data = {}
    context = {'object_list': data}
    return render(request, 'deuda/listado.html', context)

def cargar_vendedores_ajax(request):
    data = models.Vendedores.objects.using('firebird').all().order_by('nombre')
    context = {'vendedores': data}
    return render(request, 'deuda/include/cargar_vendedores.html', context)


def cargar_clientes_ajax(request):
    vendedorId = request.GET['uf']
    data = models.ClientesSucursal.objects.using('firebird').all().\
        filter(vendedores_id=vendedorId).select_related('clientes').order_by('clientes__nombre')
    context = {'clientes': data}
    return render(request, 'deuda/include/cargar_clientes.html', context)


def cargar_resultado_ajax(request):
    vendedorId = request.GET['ven']
    clienteId = request.GET['cli']
    data = {}

    if clienteId:
        data = models.DeudaView.objects.filter(vendedor=vendedorId, cliente=clienteId)
    elif vendedorId:
        data = models.DeudaView.objects.filter(vendedor=vendedorId)

    context = {'dataset': data}
    return render(request, 'deuda/include/cargar_resultado.html', context)


def info(request, filter):
    from django.urls import reverse
    return reverse('gestion:accion_deuda/'+str(filter))
