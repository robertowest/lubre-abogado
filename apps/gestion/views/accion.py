from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from apps.gestion import forms
from apps.gestion import models

paginacion = 50


class AccionListView(ListView):
    template_name = 'gestion/listado.html'

    def get_queryset(self):
        return models.Accion.objects.filter(idenc_mov=self.kwargs['filter']).order_by('fecha')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.kwargs['filter']
        return context


class AccionDetailView(DetailView):
    pass


class AccionNewView(CreateView):
    model = models.Accion
    template_name = 'gestion/formulario.html'
    form_class = forms.AccionForm

    def get_initial(self):
        return {'idenc_mov': self.kwargs['filter']}


class AccionUpdateView(UpdateView):
    model = models.Accion
    template_name = 'gestion/formulario.html'
    form_class = forms.AccionForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['previous_url'] = self.request.META.get('HTTP_REFERER')
        return context


class AccionDeleteView(DeleteView):
    pass


"""
class AccionListView(ListView):
    model = forms.Accion
    template_name = 'gestion/listado.html'
    paginate_by = paginacion

    def get_active(self, **kwargs):
        return self.filter(active=True)

    def get_queryset(self):
        queryset = models.Accion.objects.all()  # filter(pk=self.kwargs['pk'])
        return queryset


class AccionNewView(CreateView):
    model = models.Accion
    template_name = 'gestion/formulario.html'
    form_class = forms.AccionForm


class AccionDetailView(DetailView):
    model = models.Accion
    template_name = 'gestion/info.html'

    def post(self, request, *args, **kwargs):
        # comprobamos de dónde viene el post
        if request.path.find('info'):
            object = self.model.objects.get(pk=self.kwargs['pk'])
            object.delete()

        return redirect('gestion:listado')


class AccionUpdateView(UpdateView):
    model = models.Accion
    template_name = 'gestion/formulario.html'
    form_class = forms.AccionForm


class AccionDeleteView(DeleteView):
    model = models.Accion
    # template_name = 'gestion/confirmar_borrado.html'
    # success_url = reverse_lazy('gestion:listado')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('gestion:listado')
"""

