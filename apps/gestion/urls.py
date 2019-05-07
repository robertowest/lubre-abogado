from django.urls import path

from .views import home, clientecta

app_name = 'gestion'


urlpatterns = [
    # path('', home.index, name='index'),
]

# listado de comprobantes vencidos por clientes
urlpatterns += [
    path('', clientecta.index, name='clientecta'),
    path('clientecta/vendedores/ajax/', clientecta.cargar_vendedores_ajax, name='cargar_vendedores_ajax'),
    path('clientecta/clientes/ajax/', clientecta.cargar_clientes_ajax, name='cargar_clientes_ajax'),
    path('clientecta/resultado/ajax/', clientecta.cargar_resultado_ajax, name='cargar_resultado_ajax'),
    path('clientecta/<int:filter>', clientecta.info, name='accion_listado'),
]