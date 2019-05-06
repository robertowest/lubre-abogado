from django.urls import path
from . import views

app_name = 'accion'

urlpatterns = [
    path('deuda/<int:filter>', views.AccionListView.as_view(), name='listado'),
    path('deuda/<int:filter>/nuevo/', views.AccionNewView.as_view(), name='nuevo'),
    path('deuda/<int:filter>/info/<int:pk>/', views.AccionDetailView.as_view(), name='info'),
    path('deuda/<int:filter>/modif/<int:pk>/', views.AccionUpdateView.as_view(), name='modif'),
    path('deuda/<int:filter>/borrar/<int:pk>/', views.AccionDeleteView.as_view(), name='borrar'),
]