from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from apps.gestion import forms
from apps.gestion.models import accion as models
from apps.gestion.models import firebird 

paginacion = 50


class AccionListView(ListView):
    template_name = 'accion/listado.html'

    def get_queryset(self):
        return models.Accion.objects.filter(idenc_mov=self.kwargs['filter']).order_by('fecha')

    def get_context_data(self, **kwargs):
        uf = self.kwargs['filter']
        context = super().get_context_data(**kwargs)
        context['ctacte'] = firebird.CuentaCte.objects.filter(ref_idenc_mov=uf)
        context['filter'] = uf
        return context


class AccionDetailView(DetailView):
    pass


class AccionNewView(CreateView):
    model = models.Accion
    template_name = 'accion/formulario.html'
    form_class = forms.AccionForm

    def get_initial(self):
        return {'idenc_mov': self.kwargs['filter']}


class AccionUpdateView(UpdateView):
    model = models.Accion
    template_name = 'accion/formulario.html'
    form_class = forms.AccionForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['previous_url'] = self.request.META.get('HTTP_REFERER')
        return context


class AccionDeleteView(DeleteView):
    pass
