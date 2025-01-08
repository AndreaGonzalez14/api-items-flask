# API RESTfull Items

Configuración de un Proyecto Flask para una API RESTful

**¿Cómo configurarías un proyecto básico en Flask para crear una
API RESTful?**

Para configurar un proyecto básico en Flask y crear una API RESTful, primero se debe crear una carpeta para el proyecto y luego establecer un entorno virtual utilizando **python -m venv venv** para gestionar las dependencias de manera aislada. Una vez activado el entorno virtual, instala Flask y flask-restful con el comando pip install flask flask-restful. Luego, se debe crear un archivo app.py donde definirás la configuración principal de la aplicación y los endpoints necesarios utilizando la clase Resource de flask-restful.

# Requisitos

- Python 3.10
- pip install -r requirements.txt (para instalar las dependencias)
- Virtualenv (opcional)

# CRUD Items

- GET api/items: Devuelve una lista de items.
- GET api/items/<id>: Devuelve un item específico por su ID.
- POST api/items: Crea un nuevo item.
- PUT api/items/<id>: Actualiza un item por su ID.
- DELETE api/items/<id></id>: Elimina un item por su ID.

# EJEMPLOS

### 1. **GET api/items**

Obtiene una lista de todos los items disponibles.

**Descripción**: Este endpoint devuelve todos los items almacenados en memoria.

#### Ejemplo de solicitud:

```http
GET api/items
```

#### Respuesta:

```json
[
  {
    "id": 1,
    "name": "Laptop",
    "price": 800.0,
    "stock": 5,
    "available": true
  },
  {
    "id": 2,
    "name": "Phone",
    "price": 750,
    "stock": 10,
    "available": true
  }
]
```

### 2. **POST api/items**

Crea un nuevo item

**Descripción**: Este endpoint agrega un nuevo item a la lista de items en memoria

#### Ejemplo de solicitud:

```http
POST api/items
```

#### Body:

```json
{ "name": "Tablet", "price": 150, "stock": 15, "available": true }
```

#### Respuesta:

```json
[
  {
    "id": 1,
    "name": "Laptop",
    "price": 800.0,
    "stock": 5,
    "available": true
  },
  {
    "id": 2,
    "name": "Phone",
    "price": 750,
    "stock": 10,
    "available": true
  },
  {
    "id": 3,
    "name": "Tablet",
    "price": 150,
    "stock": 15,
    "available": true
  }
]
```

#### Respuesta Fallida:

Esto ocurre cuando no se cumple las condiciones para la creación del item

```json
{ "message": "Error creating new item" }
```
