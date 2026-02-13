from django.views import View
from django.http import JsonResponse, HttpResponse
from sportcore_app.application.services import PedidoService
from sportcore_app.infra.factories import PagoFactory


class ProcesarPedidoView(View):

   def get(self, request):


        service = PedidoService(
            pago_processor=PagoFactory.create()
        )

        items = [
            {"producto_id": 1, "cantidad": 2},
        ]

        pedido = service.procesar_pedido(
            cliente_id=1,
            items=items
        )

        return JsonResponse({"pedido_id": pedido.id})


class HomeView(View):
    def get(self, request):
        return HttpResponse("""
        <h1>Bienvenido a SportCore</h1>
        <p>Sistema de gestión de pedidos deportivos</p>
        <ul>
            <li><a href="/admin/">Panel de Administración</a></li>
            <li><a href="/api/pedido/">API de Pedidos</a></li>
        </ul>
        """)
