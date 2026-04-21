from django.urls import path, include
from .views import ProcesarPedidoView

urlpatterns = [
    path("pedido/", ProcesarPedidoView.as_view()),
    path('api/', include('sportcore_app.api_urls')),
]