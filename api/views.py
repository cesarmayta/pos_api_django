from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated

from .models import (
    Mesa,Categoria,
    Plato,Pedido
)

from .serializers import(
    MesaSerializer,
    CategoriaSerializer,
    PlatoSerializer,
    CategoriaPlatosSerializer,
    PedidoSerializerPOST,
    PedidoSerializerGET
)



class IndexView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self,request):
        context = {
            'ok':True,
            'content':'POS API activo'
        }

        return Response(context)

class MesaView(APIView):

    def get(self,request):
        data = Mesa.objects.all()
        serializerData = MesaSerializer(data,many=True)

        context = {
            'ok':True,
            'content':serializerData.data
        }

        return Response(context)

class CategoriaView(APIView):

    def get(self,request):
        data = Categoria.objects.all()
        serializerData = CategoriaSerializer(data,many=True)

        context = {
            'ok':True,
            'content':serializerData.data
        }

        return Response(context)

class PlatoView(APIView):

    def get(self,request):
        data = Plato.objects.all()
        serializerData = PlatoSerializer(data,many=True)

        context = {
            'ok':True,
            'content':serializerData.data
        }

        return Response(context)

class CategoriaDetail(APIView):

    def get(self,request,categoria_id):
        data = Categoria.objects.get(pk=categoria_id)
        serializerData = CategoriaSerializer(data)

        context = {
            'ok':True,
            'content':serializerData.data
        }

        return Response(context)

class CategoriaPlatosView(APIView):

    def get(self,request,categoria_id):
        data = Categoria.objects.get(pk=categoria_id)
        serializerData = CategoriaPlatosSerializer(data)

        context = {
            'ok':True,
            'content':serializerData.data
        }

        return Response(context)


class PedidoView(APIView):

    def get(self,request):
        data = Pedido.objects.all()
        serializerData = PedidoSerializerGET(data,many=True)

        context = {
            'ok':True,
            'pedidos':serializerData.data
        }

        return Response(context)

    def post(self,request):
        serializerData = PedidoSerializerPOST(data=request.data)
        serializerData.is_valid(raise_exception=True)
        serializerData.save()

        context = {
            'ok':True,
            'content':serializerData.data
        }

        return Response(context)

