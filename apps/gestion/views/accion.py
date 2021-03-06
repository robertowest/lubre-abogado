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
    """
    model = models.Accion
    template_name = 'gestion/info.html'

    def post(self, request, *args, **kwargs):
        # comprobamos de dónde viene el post
        if request.path.find('info'):
            object = self.model.objects.get(pk=self.kwargs['pk'])
            object.delete()

        return redirect('gestion:listado')
    """


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
    model = models.Accion
    template_name = 'accion/confirmar_borrado.html'

    def get_success_url(self):
        return reverse_lazy('gestion:accion_listado', kwargs={'filter': self.kwargs['filter']})


class AccionEliminarView(DeleteView):
    model = models.Accion

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('gestion:accion_listado', kwargs={'filter': self.kwargs['filter']})