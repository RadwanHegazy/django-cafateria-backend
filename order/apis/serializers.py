from rest_framework import serializers
from ..models import Order, User
from dataclasses import dataclass

@dataclass
class ViewOrdersSrz :
    user:User

    @property
    def data(self) : 
        in_cafateria = True if self.user.cafateria else False
        
        if in_cafateria : 
            orders = [
                {
                    'price' : i.product.price,
                    'order_text' : i.product.text
                } 
                for i in Order.objects.filter(cafateria=self.user.cafateria,is_recived=False)
            ]
        else:
            orders = [
                {
                    'price' : i.product.price,
                    'order_text' : i.product.text,
                    'cafateria' : i.cafateria.name,
                    'qr_path' : i.qr_path,
                } 
                for i in Order.objects.filter(user=self.user,is_recived=False)
            ]

        data = {
            'orders' : orders,
            'count' : len(orders)
        }
        return data