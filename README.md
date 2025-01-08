# API RESTfull Items

Configuración de un Proyecto Flask para una API RESTful

**¿Cómo configurarías un proyecto básico en Flask para crear una
API RESTful?**

Para configurar un proyecto básico en Flask y crear una API RESTful, primero se debe crear una carpeta para el proyecto y luego establecer un entorno virtual utilizando **python -m venv venv** para gestionar las dependencias de manera aislada. Una vez activado el entorno virtual, instala Flask y flask-restful con el comando pip install flask flask-restful. Luego, se debe crear un archivo app.py donde definirás la configuración principal de la aplicación y los endpoints necesarios utilizando la clase Resource de flask-restful.

# CRUD Items

GET /items: Devuelve una lista de items.

GET /items/<id>: Devuelve un item específico por su ID.

POST /items: Crea un nuevo item.

PUT /items/<id>: Actualiza un item por su ID.

DELETE /items/<id></id>: Elimina un item por su ID.
