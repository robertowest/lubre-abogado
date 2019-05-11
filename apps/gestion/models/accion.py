from django.db import models
from django.urls import reverse


class Accion(models.Model):
    fecha = models.DateField()
    TIPO = (('001', 'Llamada'), ('002', 'Visita'), ('003', 'Intimación'),
            ('004', 'Actuación Judicial'), ('005', 'Cobrado'))
    tipo = models.CharField(max_length=5, choices=TIPO, default='001')
    observacion = models.TextField()
    idenc_mov = models.IntegerField(null=True, blank=True)      # ctactecliresu.idenc_mov
    # idenc_mov = models.ForeignKey(CtaCteCliResu, on_delete=models.CASCADE, db_column='idenc_mov')

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('gestion:accion_listado', args=(self.idenc_mov,))

    def get_update_url(self):
        return reverse('gestion:accion_modif', args=(self.idenc_mov, self.pk,))

    def get_delete_url(self):
        return reverse('gestion:accion_borrar', args=(self.idenc_mov, self.pk,))

    def get_eliminar_url(self):
        return reverse('gestion:accion_eliminar', args=(self.idenc_mov, self.pk,))

    class Meta:
        verbose_name = 'Accion'
        verbose_name_plural = 'Acciones'