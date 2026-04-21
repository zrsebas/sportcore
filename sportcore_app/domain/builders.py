from sportcore_app.models import Pedido, DetallePedido


class PedidoBuilder:

    def __init__(self):
        self.pedido = Pedido()
        self.detalles = []

    def para_cliente(self, cliente):
        self.pedido.cliente = cliente
        return self

    def agregar_producto(self, producto, cantidad):
        detalle = DetallePedido(
            producto=producto,
            cantidad=cantidad,
            precio_unitario=producto.precio
        )
        self.detalles.append(detalle)
        return self

    def build(self):
        if not self.detalles:
            raise Exception("El pedido debe tener al menos un producto")

        self.pedido.save()

        for detalle in self.detalles:
            detalle.pedido = self.pedido
            detalle.save()

        return self.pedido
