from django.contrib import admin
from .models import Cafateria, Product


@admin.register(Cafateria)
class CafPanel (admin.ModelAdmin) : 
    list_display = ('id','name',)

@admin.register(Product)
class PdPanel (admin.ModelAdmin) : 
    list_display = ('id','text',)