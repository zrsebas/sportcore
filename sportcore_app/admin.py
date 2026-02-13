from django.contrib import admin
from .models import Categoria, Cliente, Producto, Inventario, Pedido, DetallePedido

# Register your models here.
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    search_fields = ['nombre']

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'correo', 'direccion']
    search_fields = ['nombre', 'correo']
    list_filter = ['nombre']

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio', 'categoria']
    search_fields = ['nombre']
    list_filter = ['categoria']
    list_editable = ['precio']

@admin.register(Inventario)
class InventarioAdmin(admin.ModelAdmin):
    list_display = ['producto', 'cantidad']
    search_fields = ['producto__nombre']
    list_filter = ['cantidad']

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ['id', 'cliente', 'fecha', 'estado', 'total']
    search_fields = ['cliente__nombre']
    list_filter = ['estado', 'fecha']
    readonly_fields = ['fecha', 'total']

@admin.register(DetallePedido)
class DetallePedidoAdmin(admin.ModelAdmin):
    list_display = ['pedido', 'producto', 'cantidad', 'precio_unitario']
    search_fields = ['pedido__id', 'producto__nombre']
    list_filter = ['pedido']
