from django.contrib import admin
from .models import Cafateria, Product


admin.site.register([Cafateria, Product])