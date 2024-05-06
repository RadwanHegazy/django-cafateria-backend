from django.db import models
from uuid import uuid4

class Cafateria (models.Model) : 
    name = models.CharField(max_length=225)
    id = models.UUIDField(primary_key=True,editable=False,default=uuid4)

    def __str__(self) : 
        return self.name
    

class Product (models.Model) : 
    text = models.CharField(max_length=225)
    price = models.FloatField(default=0)

    def __str__(self) -> str:
        return self.text