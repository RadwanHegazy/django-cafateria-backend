from rest_framework.urls import path
from .views import get

urlpatterns = [
    path('get/',get.get_products.as_view()),
    path('get/cafateria/',get.get_cafateria.as_view()),
]