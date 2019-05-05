from django.db import connection, connections, models


# SELECT FIRST 10 * FROM CTACTECLIRESU(3007, '2019-04-26', 1);
class CtaCteCliResu(models.Model):
    tipocomprob = models.CharField(max_length=15)
    techa = models.DateField()
    terminal = models.IntegerField()
    letra = models.CharField(max_length=1)
    numero = models.IntegerField(primary_key=True)
    cuota = models.IntegerField()
    vence = models.DateField()
    detalle = models.CharField(max_length=120)
    importe = models.FloatField()
    cliente = models.IntegerField()
    idenv_mov = models.IntegerField()
    saldo = models.FloatField()
    contador = models.IntegerField()
    idvendedor = models.IntegerField()
    nombre = models.CharField(max_length=80)
    atraso = models.IntegerField()
    dias = models.IntegerField()
    nomvendedor = models.CharField(max_length=80)

    def __str__(self):
        return '{} {} {}-{}'.format(self.TIPOCOMPROB, self.LETRA, str(self.TERMINAL).zfill(4), str(self.NUMERO).zfill(8))

    def search(param1, param2, param3):
        with connections['firebird'].cursor() as cursor:
            cursor.execute("SELECT * FROM CTACTECLIRESU(%s, %s, %s)", (param1, param2, param3,))
            results = cursor.fetchallmap()
            cursor.close()
        return results

    class Meta:
        managed = False
        db_table = 'CTACTECLIRESU'


class Clientes(models.Model):
    idcliente = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=60, blank=True, null=True)
    fantasia = models.CharField(max_length=60, blank=True, null=True)

    def __str__(self):
        return '{} ({})'.format(self.nombre, self.idcliente)

    class Meta:
        managed = False
        db_table = 'clientes'


class Vendedores(models.Model):
    idvendedor = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=60, blank=True, null=True)

    def __str__(self):
        return '{} ({})'.format(self.nombre, self.idvendedor)

    class Meta:
        managed = False
        db_table = 'vendedor'


class ClientesSucursal(models.Model):
    idclientesucursal = models.IntegerField(primary_key=True)
    clientes = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='idcliente')
    vendedores = models.ForeignKey(Vendedores, models.DO_NOTHING, db_column='idvendedor')

    class Meta:
        managed = False
        db_table = 'clientessucursal'
