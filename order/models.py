from django.db import models
from users.models import User
from cafateria.models import Product
from uuid import uuid4

class Order (models.Model) : 
    user = models.ForeignKey(User,related_name='uesr_order',on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True,editable=False,default=uuid4)
    qr_path = models.URLField(null=True,blank=True)
    recv_at = models.DateTimeField(null=True,blank=True)
    is_recived = models.BooleanField(default=False)
    product = models.ForeignKey(Product,related_name='order_pd',on_delete=models.CASCADE)
    
    def __str__(self) : 
        return str(self.id)
