from django.db import models
from users.models import User
from cafateria.models import Product
from uuid import uuid4
from django.db.models.signals import post_save
from django.dispatch import receiver
import segno

class Order (models.Model) : 
    user = models.ForeignKey(User,related_name='uesr_order',on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True,editable=False,default=uuid4)
    qr_path = models.CharField(max_length=1000,null=True,blank=True)
    recv_at = models.DateTimeField(null=True,blank=True)
    is_recived = models.BooleanField(default=False)
    product = models.ForeignKey(Product,related_name='order_pd',on_delete=models.CASCADE)
    cafateria = models.ForeignKey('cafateria.Cafateria',related_name='cafateria_order',on_delete=models.CASCADE)
    
    def __str__(self) : 
        return str(self.id)

@receiver(post_save,sender=Order)
def Create_Qr_Code (created,instance:Order,**kwargs) : 
    if created : 
        qr = segno.make_qr(str(instance.id))
        saved_path = f'media/qr-codes/{uuid4()}.png'
        qr.save(saved_path,scale=8)
        instance.qr_path = f"/{saved_path}"
        instance.save()