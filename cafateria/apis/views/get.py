from rest_framework.views import APIView
from ..serializers import ProductSerializer, Product, Cafateria, CafateriaSerializer
from rest_framework import status, response
class get_products (APIView):
    serializer_class = ProductSerializer

    def get (self,request) : 
        data = self.serializer_class(Product.objects.all(),many=True).data
        return response.Response(data,status=status.HTTP_200_OK)


class get_cafateria (APIView):
    serializer_class = CafateriaSerializer

    def get (self,request) : 
        data = self.serializer_class(Cafateria.objects.all(),many=True).data
        return response.Response(data,status=status.HTTP_200_OK)

