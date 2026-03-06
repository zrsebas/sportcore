from django.urls import path
from .api_views import PedidoAPIView

app_name = 'api'

urlpatterns = [
    path('pedidos/', PedidoAPIView.as_view(), name='pedido-list-create'),
    path('pedidos/<int:pedido_id>/', PedidoAPIView.as_view(), name='pedido-detail'),
]
