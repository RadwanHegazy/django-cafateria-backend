from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from ...models import Order
from cafateria.models import Cafateria, Product
from django.core.exceptions import ObjectDoesNotExist


class create_orders (APIView) : 
    permission_classes = [permissions.IsAuthenticated]
    
    def post (self,request,**kwargs) : 
        cafateria_id = request.data.get('cafateria',None)
        product_id = request.data.get('product',None)

        if cafateria_id is None or product_id is None :
            return Response({
                'message' : 'please enter cafateria and product ids'
            },status=status.HTTP_400_BAD_REQUEST)
            
        try :
            cafateria = Cafateria.objects.get(id=cafateria_id)
            product = Product.objects.get(id=int(product_id))
        except ObjectDoesNotExist:
            return Response({
                'message' : 'invalid cafateria or product IDs'
            },status=status.HTTP_400_BAD_REQUEST)
        
        order = Order.objects.create(
            product=product,
            cafateria=cafateria,
            user = request.user
        )
        order.save()

        return Response(status=status.HTTP_200_OK)