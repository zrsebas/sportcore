from django.views import View
from django.http import JsonResponse
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
