import django_filters

from apps.ctactecli import models

class CtaCteCliResuFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = models.CtaCteCliResu
        fields = ['cliente', 'nombre']