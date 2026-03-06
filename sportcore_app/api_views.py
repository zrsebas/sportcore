from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .application.services import PedidoService
from .infra.factories import PagoFactory
from .serializers import PedidoSerializer, PedidoCreateSerializer
from .models import Cliente, Producto, Inventario, Pedido


class PedidoAPIView(APIView):
    """
    APIView para el control total de peticiones de pedidos
    Implementa manejo correcto de códigos de estado HTTP
    """
    
    def get(self, request, pedido_id=None):
        """
        GET /api/pedidos/ - Listar todos los pedidos
        GET /api/pedidos/{id}/ - Obtener pedido específico
        """
        if pedido_id:
            try:
                pedido = Pedido.objects.get(id=pedido_id)
                serializer = PedidoSerializer(pedido)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Pedido.DoesNotExist:
                return Response(
                    {"error": "Pedido no encontrado"}, 
                    status=status.HTTP_404_NOT_FOUND
                )
        else:
            pedidos = Pedido.objects.all()
            serializer = PedidoSerializer(pedidos, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        """
        POST /api/pedidos/ - Crear nuevo pedido
        Manejo de códigos: 201, 400, 404, 409
        """
        serializer = PedidoCreateSerializer(data=request.data)
        
        if not serializer.is_valid():
            return Response(
                {"error": "Datos inválidos", "details": serializer.errors}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            # Validar cliente existe
            cliente = Cliente.objects.get(id=serializer.validated_data['cliente_id'])
            
            # Validar items
            items = serializer.validated_data['items']
            for item in items:
                producto = Producto.objects.get(id=item['producto_id'])
                if not Inventario.verificar_stock(producto, item['cantidad']):
                    return Response(
                        {"error": f"Stock insuficiente para producto {producto.nombre}"}, 
                        status=status.HTTP_409_CONFLICT
                    )
            
            # Procesar pedido
            service = PedidoService(pago_processor=PagoFactory.create())
            pedido = service.procesar_pedido(
                cliente_id=serializer.validated_data['cliente_id'],
                items=items
            )
            
            response_serializer = PedidoSerializer(pedido)
            return Response(
                response_serializer.data, 
                status=status.HTTP_201_CREATED
            )
            
        except Cliente.DoesNotExist:
            return Response(
                {"error": "Cliente no encontrado"}, 
                status=status.HTTP_404_NOT_FOUND
            )
        except Producto.DoesNotExist:
            return Response(
                {"error": "Producto no encontrado"}, 
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {"error": str(e)}, 
                status=status.HTTP_400_BAD_REQUEST
            )
