from django.urls import path
from . import views

app_name = 'ctactecli'

urlpatterns = [
    path('', views.index, name='index'),
    path('vendedores/ajax/', views.cargar_vendedores_ajax, name='cargar_vendedores_ajax'),
    path('clientes/ajax/', views.cargar_clientes_ajax, name='cargar_clientes_ajax'),
    path('resultado/ajax/', views.cargar_resultado_ajax, name='cargar_resultado_ajax'),
    path('ctactecli/<int:filter>', views.info, name='info'),
]