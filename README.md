# Proyecto de Gestión de Pedidos

## Estructura del Proyecto

📦src
┣ 📂models
┃ ┣ 📜cliente.py
┃ ┣ 📜pedido.py
┃ ┣ 📜roles.py
┃ ┣ 📜usuario.py
┣ 📂routes
┃ ┣ 📜clientes.py
┃ ┣ 📜clientes_bp.py
┃ ┣ 📜pedidos.py
┃ ┣ 📜pedidos_bp.py
┃ ┣ 📜roles.py
┃ ┣ 📜roles_bp.py
┃ ┣ 📜usuarios.py
┃ ┗ 📜usuarios_bp.py
┣ 📜app.py
┣ 📜config.py

## APIS

### Operaciones CRUD para la Entidad Cliente:

1. **Crear un Cliente:**

   - Método: POST
   - Ruta: `/clientes`
   - Parámetros de Entrada (JSON):
     - `nombre` (String): Nombre del cliente (Requerido).
     - `apellido` (String): Apellido del cliente (Requerido).
     - `direccion` (String): Dirección del cliente (Requerido).
     - `telefono` (String): Número de teléfono del cliente (Requerido y único).
     - `detalle` (String): Detalles adicionales del cliente (Requerido).
     - `otro` (String, Opcional): Otros detalles opcionales del cliente.

2. **Obtener Todos los Clientes:**

   - Método: GET
   - Ruta: `/clientes`
   - Parámetros de Entrada: No se requieren parámetros.

3. **Obtener Cliente por Teléfono:**

   - Método: GET
   - Ruta: `/clientes/telefonoCliente/{telefono}`
   - Parámetros de Entrada:
     - `telefono` (String): Número de teléfono del cliente a buscar (Requerido).

4. **Actualizar un Cliente por Teléfono:**

   - Método: PUT
   - Ruta: `/clientes/telefonoCliente/{telefono}`
   - Parámetros de Entrada (JSON):
     - `nombre` (String, Opcional): Nuevo nombre del cliente.
     - `apellido` (String, Opcional): Nuevo apellido del cliente.
     - `direccion` (String, Opcional): Nueva dirección del cliente.
     - `telefono` (String, Opcional): Nuevo número de teléfono del cliente.
     - `detalle` (String, Opcional): Nuevos detalles adicionales del cliente.
     - `otro` (String, Opcional): Nuevos detalles opcionales del cliente.

5. **Eliminar un Cliente por Teléfono:**
   - Método: DELETE
   - Ruta: `/clientes/telefonoCliente/{telefono}`
   - Parámetros de Entrada:
     - `telefono` (String): Número de teléfono del cliente a eliminar (Requerido).

### Operaciones CRUD para la Entidad Pedido:

6. **Crear un Pedido:**

   - Método: POST
   - Ruta: `/pedidos`
   - Parámetros de Entrada (JSON):
     - `idCliente` (Número): ID interno del cliente al que se asocia el pedido (Requerido, pero el usuario no lo conoce).
     - `direccion` (String): Dirección de entrega del pedido (Requerido).
     - `fecha` (String): Fecha del pedido en formato "DD/MM/YYYY HH:MM" (Requerido).
     - `pedido` (String): Detalles del pedido (Requerido).
     - `movil` (String): Número de teléfono de contacto para el pedido (Requerido).
     - `tipoPago` (String): Método de pago para el pedido (Requerido).
     - `estado` (String): Estado del pedido (Requerido).
     - `local` (String): Local de origen del pedido (Requerido).
     - `otro` (String, Opcional): Otros detalles opcionales del pedido.

7. **Obtener Todos los Pedidos:**

   - Método: GET
   - Ruta: `/pedidos`
   - Parámetros de Entrada: No se requieren parámetros.

8. **Obtener Pedido por Número de Pedido:**

   - Método: GET
   - Ruta: `/pedidos/{nroPedido}`
   - Parámetros de Entrada:
     - `nroPedido` (Número): Número de pedido a buscar (Requerido).

9. **Actualizar un Pedido por Número de Pedido:**

   - Método: PUT
   - Ruta: `/pedidos/{nroPedido}`
   - Parámetros de Entrada (JSON):
     - `idCliente` (Número, Opcional): Nuevo ID interno del cliente asociado al pedido.
     - `direccion` (String, Opcional): Nueva dirección de entrega del pedido.
     - `fecha` (String, Opcional): Nueva fecha del pedido en formato "DD/MM/YYYY HH:MM".
     - `pedido` (String, Opcional): Nuevos detalles del pedido.
     - `movil` (String, Opcional): Nuevo número de teléfono de contacto para el pedido.
     - `tipoPago` (String, Opcional): Nuevo método de pago para el pedido.
     - `estado` (String, Opcional): Nuevo estado del pedido.
     - `local` (String, Opcional): Nuevo local de origen del pedido.
     - `otro` (String, Opcional): Nuevos detalles opcionales del pedido.

10. **Eliminar un Pedido por Número de Pedido:**
    - Método: DELETE
    - Ruta: `/pedidos/{nroPedido}`
    - Parámetros de Entrada:
      - `nroPedido` (Número): Número de pedido a eliminar (Requerido).

### Operaciones CRUD para la Entidad Usuario:

1. **Crear un Usuario:**

   - Método: POST
   - Ruta: `/usuarios`
   - Parámetros de Entrada (JSON):
     - `username` (String): Nombre de usuario (Requerido).
     - `password` (String): Contraseña del usuario (Requerido).

2. **Obtener Todos los Usuarios:**

   - Método: GET
   - Ruta: `/usuarios`
   - Parámetros de Entrada: No se requieren parámetros.

3. **Obtener Usuario por ID:**

   - Método: GET
   - Ruta: `/usuarios/{id}`
   - Parámetros de Entrada:
     - `id` (Int): ID del usuario a buscar (Requerido).

4. **Actualizar un Usuario por ID:**

   - Método: PUT
   - Ruta: `/usuarios/{id}`
   - Parámetros de Entrada (JSON):
     - Campos opcionales dependiendo de lo que se desee actualizar.

5. **Eliminar un Usuario por ID:**
   - Método: DELETE
   - Ruta: `/usuarios/{id}`
   - Parámetros de Entrada:
     - `id` (Int): ID del usuario a eliminar (Requerido).

### Operaciones CRUD para la Entidad Rol:

1. **Crear un Rol:**

   - Método: POST
   - Ruta: `/roles`
   - Parámetros de Entrada (JSON):
     - `nombre` (String): Nombre del rol (Requerido).

2. **Obtener Todos los Roles:**

   - Método: GET
   - Ruta: `/roles`
   - Parámetros de Entrada: No se requieren parámetros.

3. **Obtener Rol por ID:**

   - Método: GET
   - Ruta: `/roles/{id}`
   - Parámetros de Entrada:
     - `id` (Int): ID del rol a buscar (Requerido).

4. **Actualizar un Rol por ID:**

   - Método: PUT
   - Ruta: `/roles/{id}`
   - Parámetros de Entrada (JSON):
     - `nombre` (String, Opcional): Nuevo nombre del rol.

5. **Eliminar un Rol por ID:**
   - Método: DELETE
   - Ruta: `/roles/{id}`
   - Parámetros de Entrada:
     - `id` (Int): ID del rol a eliminar (Requerido).

### Seguridad

- Implementación de JWT (JSON Web Tokens) para la autenticación y protección de rutas.
- Rutas protegidas que requieren un token JWT válido para acceder.
