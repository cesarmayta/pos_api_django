from email.policy import default
from django.db import models

from cloudinary.models import CloudinaryField

from django.contrib.auth.models import User

# Create your models here.
class Mesa(models.Model):
    mesa_id = models.AutoField(primary_key=True)
    mesa_nro = models.CharField(max_length=10,verbose_name='Nro Mesa')
    mesa_cap = models.IntegerField(default=0,verbose_name='Capacidad')

    class Meta:
        db_table = 'tbl_mesa'

    def __str__(self):
        return self.mesa_nro

class Categoria(models.Model):
    categoria_id = models.AutoField(primary_key=True)
    categoria_nom = models.CharField(max_length=100,verbose_name='Nombre')

    class Meta:
        db_table = 'tbl_categoria'

    def __str__(self):
        return self.categoria_nom

class Plato(models.Model):
    plato_id = models.AutoField(primary_key=True)
    plato_nom = models.CharField(max_length=200,verbose_name='Nombre')
    plato_img = CloudinaryField('image',default='')
    plato_pre = models.DecimalField(max_digits=10,decimal_places=2,default=0,verbose_name='Precio')
    categoria_id = models.ForeignKey(Categoria,related_name='Platos',
                                    to_field='categoria_id',on_delete=models.RESTRICT,
                                    db_column='categoria_id',verbose_name='Categoria')

    class Meta:
        db_table = 'tbl_plato'

    def __str__(self):
        return self.plato_nom

class Pedido(models.Model):

    ESTADO_CHOICES = (
        ('solicitado','Solicitado'),
        ('entregado','entregado')
    )

    pedido_id = models.AutoField(primary_key=True)
    pedido_fech = models.DateTimeField(null=True,verbose_name='Fecha')
    pedido_nro = models.CharField(max_length=100,default='',verbose_name='Nro Pedido')
    pedido_est = models.CharField(max_length=100,default='solicitado',
                                  choices=ESTADO_CHOICES,verbose_name='Estado')
    mesa_id = models.ForeignKey(Mesa,to_field='mesa_id',on_delete=models.RESTRICT,
                               db_column='mesa_id',verbose_name='Nro Mesa')
    usu_id = models.ForeignKey(User,to_field='id',related_name='Pedidos',
                               on_delete=models.RESTRICT,
                               db_column='usu_id',verbose_name='Usuario')

    class Meta:
        db_table = 'tbl_pedido'

    def __str__(self):
        return self.pedido_nro

class PedidoPlato(models.Model):
    pedidoplato_id = models.AutoField(primary_key=True)
    pedidoplato_cant = models.IntegerField(default=1,verbose_name='Cantidad')
    plato_id = models.ForeignKey(Plato,related_name='pedidoplatos',to_field='plato_id',
                                on_delete=models.RESTRICT,db_column='plato_id',
                                verbose_name='Plato')
    pedido_id = models.ForeignKey(Pedido,related_name='pedidoplatos',to_field='pedido_id',
                                on_delete=models.RESTRICT,db_column='pedido_id',
                                verbose_name='Pedido')

    class Meta:
        db_table = 'tbl_pedido_plato'

    def __str__(self):
        return str(self.plato_id)

    
