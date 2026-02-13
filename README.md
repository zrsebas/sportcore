# SportCore - Sistema de Gestión de Pedidos Deportivos

Proyecto Django para la gestión de pedidos de productos deportivos con arquitectura limpia.

## 🚀 Características

- **Gestión de Categorías**: Organiza tus productos deportivos por categorías
- **Gestión de Clientes**: Registro y gestión de clientes
- **Gestión de Productos**: Catálogo de productos con precios y descripciones
- **Control de Inventario**: Seguimiento de stock en tiempo real
- **Sistema de Pedidos**: Creación y gestión de pedidos
- **API REST**: Endpoint para procesamiento de pedidos
- **Panel de Administración**: Interfaz Django Admin completa

## 📋 Modelos de Datos

- **Categorías**: Clasificación de productos
- **Clientes**: Información de clientes
- **Productos**: Catálogo de artículos deportivos
- **Inventarios**: Control de stock
- **Pedidos**: Gestión de órdenes
- **DetallePedidos**: Items de cada pedido

## 🛠️ Instalación

1. Clonar el repositorio
2. Crear entorno virtual: `python -m venv venv`
3. Activar entorno: `venv\Scripts\activate` (Windows)
4. Instalar dependencias: `pip install django==6.0.2`
5. Migrar la base de datos: `python manage.py migrate`
6. Crear superusuario: `python manage.py createsuperuser`
7. Iniciar servidor: `python manage.py runserver`

## 🔐 Acceso por Defecto

- **URL**: http://127.0.0.1:8000
- **Admin**: http://127.0.0.1:8000/admin
- **API**: http://127.0.0.1:8000/api/pedido/

## 📊 Arquitectura

```
sportcore/
├── config/          # Configuración Django
├── sportcore_app/   # Aplicación principal
│   ├── application/ # Lógica de negocio
│   ├── domain/      # Modelos de dominio
│   └── infra/       # Infraestructura
├── venv/           # Entorno virtual
└── db.sqlite3      # Base de datos
```

## 🏃‍♂️ Uso

1. Accede al panel de admin para gestionar datos
2. Crea categorías, productos y clientes
3. Gestiona el inventario
4. Procesa pedidos vía API
5. Monitorea el estado de los pedidos

## 📝 Ejemplos

### API de Pedidos
```bash
GET http://127.0.0.1:8000/api/pedido/
# Respuesta: {"pedido_id": 1}
```

## 🤝 Contribución

1. Fork del proyecto
2. Crear feature branch
3. Commit changes
4. Push to branch
5. Pull Request

## 📄 Licencia

MIT License
