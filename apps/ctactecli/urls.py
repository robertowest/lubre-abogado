from django.urls import path

from apps.ctactecli.views import ctactecli
from apps.ctactecli.views import accion

app_name = 'ctactecli'

# cuentas corrientes de clientes
urlpatterns = [
    path('', ctactecli.index, name='index'),
    path('vendedores/ajax/', ctactecli.cargar_vendedores_ajax, name='cargar_vendedores_ajax'),
    path('clientes/ajax/', ctactecli.cargar_clientes_ajax, name='cargar_clientes_ajax'),
    path('resultado/ajax/', ctactecli.cargar_resultado_ajax, name='cargar_resultado_ajax'),
    # path('ctactecli/<int:filter>', ctactecli.info, name='info'),
]

# acciones sobre deuda
urlpatterns += [
    path('ctactecli/<int:filter>', accion.AccionListView.as_view(), name='accion_listado'),
    path('ctactecli/<int:filter>/nuevo/', accion.AccionNewView.as_view(), name='accion_nuevo'),
    path('ctactecli/<int:filter>/info/<int:pk>/', accion.AccionDetailView.as_view(), name='accion_info'),
    path('ctactecli/<int:filter>/modif/<int:pk>/', accion.AccionUpdateView.as_view(), name='accion_modif'),
    path('ctactecli/<int:filter>/borrar/<int:pk>/', accion.AccionDeleteView.as_view(), name='accion_borrar'),
]