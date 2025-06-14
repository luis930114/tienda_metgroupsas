﻿# tienda_metgroupsas


## API flask tienda y articulos

Esta es una API RESTful desarrollada con Flask, que utiliza SQLite como base de datos y sigue buenas prácticas de desarrollo como el uso de Blueprints, principios ACID en las transacciones, y separación modular de la lógica.

Provee endpoints para:

- Registro y autenticación de usuarios
- CRUD de tiendas
- CRUD de artículos
- Protección de rutas con JWT

## Configuración 
Para poder correr el proyecto se tiene dos opciones una es utilizar un contenedor docker y otra es de manera local

### Instalación

- clonar repositorio:
```bash
    git clone https://github.com/luis930114/tienda_metgroupsas.git
```

o si tiene clave ssh:
```bash
    git clone git@github.com:luis930114/tienda_metgroupsas.git
```

- Acceder a la carpeta del proyecto
```bash
    cd tienda_metgroupsas
```

- Construir un archivo .env.prod 

```bash
ENVIRONMENT=production
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=metgroupsas_db
DATABASE_URL=postgresql://postgres:postgres@db:5432/metgroupsas_db
```

- Correr el proyecto con docker-compose.
```bash
    docker-compose up --build
```

- Accede a la API desde Postman:
```bash
    http://localhost:5000
```

## API Reference

### Crear un nuevo usuario.

```http
  POST /register
  Crear un nuevo usuario
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `username` | `string` | **Required**. Your username |
| `password` | `string` | **Required**. Your username |


### Loguearse con el usuario.

```http
  POST /auth
  Loguearse con el usuario
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `username` | `string` | **Required**. Your username |
| `password` | `string` | **Required**. Your username |

### Crear nueva tienda.

```http
  POST /store/<string:name>
  Crear nueva tienda.
```

### Ver nueva tienda.

```http
  GET /store/<string:name>
  Ver nueva tienda.
```

### Eliminar tienda.

```http
  DELETE /store/<string:name>
  Eliminar tienda.
```

### Ver todas las tiendas creadas.

```http
  GET /stores
  Ver todas las tiendas creadas
```

### Crear nuevo articulo.

```http
  POST /item/<string:name>
  Crear nuevo articulo.
```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `price` | `integer` | **Required**. Price item |
| `store_id` | `integer` | **Required**. id of the store to the belonged item |


### Ver nuevo articulo.

```http
  GET /item/<string:name>
  Ver nuevo articulo.
```
| Header | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `authorization` | `integer` | **Required**. authentication user |

### Actualizar un articulo.

```http
  PUT /item/<string:name>
  Actualizar un articulo.
```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `price` | `integer` | **Required**. Price item |
| `store_id` | `integer` | **Required**. id of the store to the belonged item |

### Eliminar articulo.

```http
  DELETE /item/<string:name>
  Eliminar articulo.
```

### Ver todos los articulos creados

```http
  GET /items
  Ver todos los articulos creados
```

## Authors

- [@luis930114](https://github.com/luis930114)


