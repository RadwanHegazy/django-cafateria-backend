from ..models import Product, Cafateria
from rest_framework import serializers

class ProductSerializer (serializers.ModelSerializer) : 
    class Meta:
        model = Product
        fields = ('id','text','price',)

    def to_representation(self, instance:Product):
        return {
            'text' : f'{instance.text} -> {instance.price}',
            'id' : instance.id
        }
    
class CafateriaSerializer (serializers.ModelSerializer) : 
    class Meta:
        model = Cafateria
        fields = ('id','name',)