from django.urls import path
from .views import ProcesarPedidoView

urlpatterns = [
    path("pedido/", ProcesarPedidoView.as_view()),
]