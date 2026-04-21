from sportcore_app.domain.builders import PedidoBuilder
from sportcore_app.models import Inventario, Cliente, Producto


class PedidoService:

    def __init__(self, pago_processor):
        self.pago_processor = pago_processor

    def procesar_pedido(self, cliente_id, items):

        cliente = Cliente.objects.get(id=cliente_id)

        builder = PedidoBuilder().para_cliente(cliente)

        for item in items:
            producto_id = item["producto_id"]
            cantidad = item["cantidad"]

            producto = Producto.objects.get(id=producto_id)

            if not Inventario.verificar_stock(producto, cantidad):
                raise Exception("Stock insuficiente")

            builder.agregar_producto(producto, cantidad)

        pedido = builder.build()

        pedido.calcular_total()

        self.pago_processor.procesar(pedido.total)

        pedido.confirmar_pedido()

        return pedido
