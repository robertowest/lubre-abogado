from django.http import JsonResponse

from .models import Clientes, ClientesSucursal


"""
from apps.ctactecli import models
result = models.ClientesSucursal.objects.using('firebird').filter(idcliente=9132)
obj = result.select_related('idcliente', 'idvendedor')
print(result[0])
print(obj[0].idcliente.nombre)
"""

def get_clientes(request):
    response = {}
    return JsonResponse(response)


def get_clientes_old(request):
    vendedor_id = request.GET.get('vendedor_id')
    clientes = Clientes.objects.using('firebird').none()

    options = '<option value="" selected="selected">---------</option>'
    if vendedor_id:
        relacion = ClientesSucursal.objects.using('firebird')\
                    .filter(idvendedor=vendedor_id)\
                    .select_related('idvendedor')
    for rela in relacion:
        options += '<option value="%s">%s</option>' % (
            rela.idvendedor.idvendedor,
            rela.idvendedor.nombre
        )
    response = {}
    response['vendedores'] = options
    return JsonResponse(response)



"""
def get_localidades(request):
    municipio_id = request.GET.get('municipio_id')
    localidades = Localidad.objects.none()
    options = '<option value="" selected="selected">---------</option>'
    if municipio_id:
        localidades = Localidad.objects.filter(municipio_id=municipio_id)   
    for localidad in localidades:
        options += '<option value="%s">%s</option>' % (
            localidad.pk,
            localidad.localidad
        )
    response = {}
    response['localidades'] = options
    return JsonResponse(response)
"""