
from rest_framework import serializers

from .models import (
    Mesa,Categoria, Plato
    ,Pedido,PedidoPlato
)

from django.contrib.auth.models import User

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class MesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mesa
        fields = '__all__'

class PlatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plato
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['plato_img'] = instance.plato_img.url
        return representation

class CategoriaPlatosSerializer(serializers.ModelSerializer):
    Platos = PlatoSerializer(many=True,read_only=True)
    class Meta:
        model = Categoria
        fields = ['categoria_id','categoria_nom','Platos']

class PedidoPlatoSerializerPOST(serializers.ModelSerializer):
    class Meta:
        model = PedidoPlato
        fields = ['plato_id','pedidoplato_cant']

class PedidoSerializerPOST(serializers.ModelSerializer):
    pedidoplatos = PedidoPlatoSerializerPOST(many=True)

    class Meta:
        model = Pedido
        fields = ['pedido_fech','pedido_nro','pedido_est','usu_id','mesa_id','pedidoplatos']

    def create(self,validated_data):
        pedidos_data = validated_data.pop('pedidoplatos')
        pedido  = Pedido.objects.create(**validated_data)
        for pedido_data in pedidos_data:
            PedidoPlato.objects.create(pedido_id=pedido,**pedido_data)
        return pedido
    
class PedidoPlatoSerializerGET(serializers.ModelSerializer):
    class Meta:
        model = PedidoPlato
        fields = ['pedidoplato_id','pedidoplato_cant','pedido_id','plato_id']

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ''

    def to_representation(self, instance):
        representation =  super().to_representation(instance)
        representation['usu_id'] = instance.id
        representation['usu_email'] = instance.email
        representation['usu_nom'] =  instance.first_name
        representation['usu_ape'] = instance.last_name
        if instance.is_superuser == 1:
            representation['usu_tipo'] = 'admin'
        else:
            representation['usu_tipo'] = 'mozo'
        return representation

class PedidoSerializerGET(serializers.ModelSerializer):
    pedidoplatos = PedidoPlatoSerializerGET(many=True,read_only=True)

    class Meta:
        model = Pedido
        fields = ['pedido_id','pedido_fech','pedido_nro','pedido_est','usu_id','mesa_id','pedidoplatos']

    def to_representation(self, instance):
        representation =  super().to_representation(instance)
        serializerMesa = MesaSerializer(instance.mesa_id)
        representation['Mesa'] = serializerMesa.data
        serializerUsuario = UsuarioSerializer(instance.usu_id)
        representation['Usuario'] = serializerUsuario.data
        return representation
