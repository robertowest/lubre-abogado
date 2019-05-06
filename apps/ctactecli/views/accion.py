from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from apps.ctactecli import forms
from apps.ctactecli.models import accion as models

paginacion = 50


class AccionListView(ListView):
    template_name = 'accion/listado.html'

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
