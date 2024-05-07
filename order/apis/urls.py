from django.urls import path
from .views import get, create

urlpatterns = [
    path('get/',get.get_orders.as_view()),
    path('scan/<str:order_id>/',get.scan_order.as_view()),
    path('create/',create.create_orders.as_view())
]