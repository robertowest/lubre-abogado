from django.http import request
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from datetime import datetime

from apps.ctactecli import models
from apps.ctactecli import filters

# import pdb; pdb.set_trace()

paginacion = 20


def busqueda(request):
    # f = filters.CtaCteCliResuFilter(request.GET, queryset=models.CtaCteCliResu.objects.all())
    result = models.CtaCteCliResu.search(-1, datetime.now(), 0)
    f = filters.CtaCteCliResuFilter(request.GET, queryset=result)
    return render(request, 'ctactecliresu/busqueda.html', {'filter': f})


def filtro(request):
    return render(request, 'ctactecliresu/filtro.html', {'nombre': 'olga'})


class listado(ListView):
    model = models.CtaCteCliResu
    template_name = 'ctactecliresu/listado.html'
    paginate_by = paginacion
    # request.GET['param1']
    # queryset = model.search('9893', datetime.now().strftime('%Y-%m-%d'), 1)
    # queryset = model.search(param1=-1, param2=datetime.now(), param3=1)

    def get_context_data(self, **kwargs):
        context = super(listado, self).get_context_data(**kwargs)
        context['vendedores'] = models.Vendedores.objects.using('firebird').all().order_by('nombre')
        context['clientes'] = models.Clientes.objects.using('firebird').all().order_by('nombre')
        # models.Clientes.objects.all().filter(idvendedor=?).order_by('nombre')
        return context

    def get_queryset(self):
        if self.request.GET.get("cliente_id"):
            id = self.request.GET.get("cliente_id")
            queryset = self.model.search(param1=id, param2=datetime.now(), param3=1)
        else:
            queryset = self.model.search(param1=-1, param2=datetime.now(), param3=1)
        return queryset


class detalle(DetailView):
    model = models.CtaCteCliResu
    template_name = 'ctactecliresu/info.html'


class filtro(ListView):
    model = models.CtaCteCliResu
    template_name = 'ctactecliresu/busqueda.html'

    def get_context_data(self, **kwargs):
        context = super(filtro, self).get_context_data(**kwargs)
        context['vendedores'] = models.Vendedores.objects.using('firebird').all().order_by('nombre')
        context['clientes'] = models.Clientes.objects.using('firebird').all().order_by('nombre')
        # models.Clientes.objects.all().filter(idvendedor=?).order_by('nombre')
        return context

    def get_queryset(self):
        if self.request.GET.get("browse"):
            id = self.request.GET.get("browse")
            queryset = self.model.search(param1=id, param2=datetime.now(), param3=1)
        else:
            queryset = self.model.search(param1=-1, param2=datetime.now(), param3=1)

        return queryset




from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import PruebaForm

def prueba(request):
    form = PruebaForm
    if request.method == 'POST':
        form = PruebaForm(request.POST)
        if form.is_valid():
            # Guardar los datos
            url = reverse('home')
            return HttpResponseRedirect(url)
    return render(request, 'prueba.html', {'form': form})