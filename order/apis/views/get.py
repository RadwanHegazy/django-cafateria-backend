from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from ...models import Order
# from datetime import datetime,timezone
from django.utils.timezone import datetime
from users.models import User
from ..serializers import ViewOrdersSrz


class scan_order (APIView) : 

    def get(self,request,order_id) : 
        if request.user.cafateria is None:
            return Response(status=status.HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS)
        

        try :
            order = Order.objects.get(id=order_id)
        except Order.DoesNotExist:
            return Response({
                'message' : 'invalid qr code'
            },status=status.HTTP_404_NOT_FOUND)

        if order.cafateria != request.user.cafateria :
            return Response(status=status.HTTP_400_BAD_REQUEST)


        if order.is_recived :
            return Response({
                'message' : 'order already taken'
            },status=status.HTTP_404_NOT_FOUND)
        

        order.is_recived = True
        order.recv_at = datetime.now()
        order.save()

        data = {
            'user_pic' : order.user.picture.url,
            'user':order.user.full_name,
            'price' : order.product.price,
            'order' : order.product.text, 
        }
        return Response(data,status=status.HTTP_200_OK)

class get_orders (APIView) : 
    permission_classes = [permissions.IsAuthenticated]
    
    def get (self,request,**kwargs) : 
        user = request.user
        serializer = ViewOrdersSrz(user=user)
        return Response(serializer.data,status=status.HTTP_200_OK)