from datetime import datetime
from django.shortcuts import render
from django.urls import reverse

from apps.gestion.models import firebird as models


def index(request):
    context = {}
    context = {}
    # context['dataset'] = models.DeudaView.objects.filter(idenc_mov=filter)
    return render(request, 'deuda/listado.html', context)


# TODO: fusionar con index (index2 debe desaparecer)
def index2(request, filter):
    # import pdb; pdb.set_trace()
    import json
    data = models.DeudaView.objects.filter(idenc_mov=filter)
    context = {}
    context['dataset'] = data
    context['json_data'] = json.dumps({
        'vendedor':data[0].vendedor.idvendedor, 
        'cliente':data[0].cliente.idcliente
    })
    return render(request, 'deuda/listado2.html', context)


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
