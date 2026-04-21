from django.contrib import admin
from django.urls import path, include
from sportcore_app.views import HomeView, ProcesarPedidoView

urlpatterns = [
    path('', HomeView.as_view()),
    path('admin/', admin.site.urls),
    path('api/', include('sportcore_app.api_urls')),
    path('api/pedido/', ProcesarPedidoView.as_view()),
]
