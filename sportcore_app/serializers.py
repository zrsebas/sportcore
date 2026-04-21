from rest_framework import serializers
from .models import Categoria, Cliente, Producto, Inventario, Pedido, DetallePedido


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nombre']


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nombre', 'correo', 'direccion']


class ProductoSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer(read_only=True)
    
    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'precio', 'descripcion', 'categoria']


class InventarioSerializer(serializers.ModelSerializer):
    producto = ProductoSerializer(read_only=True)
    
    class Meta:
        model = Inventario
        fields = ['producto', 'cantidad']


class DetallePedidoSerializer(serializers.ModelSerializer):
    producto = ProductoSerializer(read_only=True)
    
    class Meta:
        model = DetallePedido
        fields = ['pedido', 'producto', 'cantidad', 'precio_unitario']


class PedidoSerializer(serializers.ModelSerializer):
    cliente = ClienteSerializer(read_only=True)
    detallepedido_set = DetallePedidoSerializer(many=True, read_only=True)
    
    class Meta:
        model = Pedido
        fields = ['id', 'cliente', 'fecha', 'estado', 'total', 'detallepedido_set']


class PedidoCreateSerializer(serializers.Serializer):
    cliente_id = serializers.IntegerField()
    items = serializers.ListField(
        child=serializers.DictField(child=serializers.IntegerField())
    )
    
    def validate_cliente_id(self, value):
        if not Cliente.objects.filter(id=value).exists():
            raise serializers.ValidationError("Cliente no encontrado")
        return value
    
    def validate_items(self, items):
        if not items:
            raise serializers.ValidationError("Debe incluir al menos un item")
        return items
