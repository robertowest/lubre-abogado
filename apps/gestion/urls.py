from django.urls import path

from .views import home, clientecta, accion

app_name = 'gestion'


urlpatterns = [
    # path('', home.index, name='index'),
]

# listado de comprobantes vencidos por clientes
urlpatterns += [
    path('', clientecta.index, name='clientecta'),
    path('clientecta/<int:filter>/', clientecta.index2, name='cargar_clientecta'),

    path('clientecta/vendedores/ajax/', clientecta.cargar_vendedores_ajax, name='cargar_vendedores_ajax'),
    path('clientecta/clientes/ajax/', clientecta.cargar_clientes_ajax, name='cargar_clientes_ajax'),
    path('clientecta/resultado/ajax/', clientecta.cargar_resultado_ajax, name='cargar_resultado_ajax'),
]

# acciones sobre deuda
urlpatterns += [
    path('clientecta/accion/<int:filter>', accion.AccionListView.as_view(), name='accion_listado'),
    path('clientecta/accion/<int:filter>/nuevo/', accion.AccionNewView.as_view(), name='accion_nuevo'),
    path('clientecta/accion/<int:filter>/info/<int:pk>/', accion.AccionDetailView.as_view(), name='accion_info'),
    path('clientecta/accion/<int:filter>/modif/<int:pk>/', accion.AccionUpdateView.as_view(), name='accion_modif'),
    path('clientecta/accion/<int:filter>/borrar/<int:pk>/', accion.AccionDeleteView.as_view(), name='accion_borrar'),
]
