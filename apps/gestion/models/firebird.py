from django.db import models
from django.urls import reverse


class Vendedores(models.Model):
    idvendedor = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vendedor'
        app_label = 'firebird'
        verbose_name = 'Vendedor'
        verbose_name_plural = 'Vendedores'


class Actividades(models.Model):
    idactividad = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'actividades'
        app_label = 'firebird'
        verbose_name = 'Actividad'
        verbose_name_plural = 'Actividades'


class Califica(models.Model):
    idcalifica = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'califica'
        app_label = 'firebird'


class Estadocliente(models.Model):
    idestadocliente = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=40, blank=True, null=True)
    fechaalta = models.DateTimeField(blank=True, null=True)
    datospc = models.CharField(max_length=60, blank=True, null=True)
    idopera = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estadocliente'
        app_label = 'firebird'


class Clientes(models.Model):
    idcliente = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=60, blank=True, null=True)
    fantasia = models.CharField(max_length=60, blank=True, null=True)
    idactividad = models.ForeignKey(Actividades, models.DO_NOTHING, db_column='idactividad')
    idcalifica = models.ForeignKey(Califica, models.DO_NOTHING, db_column='idcalifica')
    idestadocliente = models.ForeignKey('Estadocliente', models.DO_NOTHING, db_column='idestadocliente')
    direc_d = models.CharField(max_length=60, blank=True, null=True)
    directivos = models.CharField(max_length=60, blank=True, null=True)
    telef_d = models.CharField(max_length=20, blank=True, null=True)
    email_d = models.CharField(max_length=90, blank=True, null=True)
    idprovincias = models.CharField(max_length=15, blank=True, null=True)
    localidad = models.CharField(max_length=60, blank=True, null=True)
    direccion = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clientes'
        app_label = 'firebird'
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'


class CuentaCte(models.Model):
    idcuentacte = models.IntegerField(primary_key=True)
    idcliente = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='idcliente')
    tipocomprob = models.CharField(max_length=15, blank=True, null=True)
    letra = models.CharField(max_length=1, blank=True, null=True)
    terminal = models.IntegerField(blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    vence = models.DateField(blank=True, null=True)
    importe = models.FloatField(blank=True, null=True)
    idenc_mov = models.IntegerField(blank=True, null=True)
    ref_idenc_mov = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cuentacte'
        app_label = 'firebird'


class ClientesSucursal(models.Model):
    idclientesucursal = models.IntegerField(primary_key=True)
    clientes = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='idcliente')
    vendedores = models.ForeignKey(Vendedores, models.DO_NOTHING, db_column='idvendedor')

    class Meta:
        managed = False
        db_table = 'clientessucursal'
        app_label = 'ctactecli'


# -----------------------------------------------------------------------------
# vistas personalizadas
# -----------------------------------------------------------------------------

class DeudaView(models.Model):
    vendedor = models.ForeignKey(Vendedores, models.DO_NOTHING, db_column='idvendedor')
    cliente = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='idcliente')
    comprobante = models.CharField(max_length=20, blank=True, null=True)
    idenc_mov = models.IntegerField(primary_key=True)
    total = models.FloatField(blank=True, null=True)
    meses = models.IntegerField(blank=True, null=True)
    dias = models.IntegerField(blank=True, null=True)

    class Meta:
        default_permissions = ('view')
        managed = False
        db_table = 'deuda_cliente_vendedor_v'
        app_label = 'firebird'
        verbose_name = 'Deuda'
        verbose_name_plural = 'Deudas'
