from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    direccion = models.CharField(max_length=200)


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.FloatField()
    descripcion = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)


class Inventario(models.Model):
    producto = models.OneToOneField(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    @staticmethod
    def verificar_stock(producto, cantidad):
        inventario = Inventario.objects.get(producto=producto)
        return inventario.cantidad >= cantidad


class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=50, default="CREADO")
    total = models.FloatField(default=0)

    def calcular_total(self):
        detalles = self.detallepedido_set.all()
        self.total = sum(d.cantidad * d.precio_unitario for d in detalles)
        self.save()

    def confirmar_pedido(self):
        self.estado = "CONFIRMADO"
        self.save()


class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario = models.FloatField()
