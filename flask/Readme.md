🎯 Objetivo del sistema:
Permitir a pequeños negocios emitir facturas digitales de manera sencilla, registrar ventas, clientes y productos, y generar reportes básicos.

🧩 Módulos principales:
1. Autenticación y Usuarios
-   Registro de usuarios.
-   Roles: admin (acceso total), vendedor (acceso limitado).
-   Seguridad básica con hash de contraseñas.

2. Gestión de Productos
-   CRUD de productos.
    Campos: 
    * nombre
    * descripción
    * precio unitario
    * stock
    * unidad de medida
    * categoría.

3. Gestión de Clientes
-   CRUD de clientes.
    Campos: 
    * nombre
    * dirección
    * telefono
    * correo electrónico
    * fecha de nacimiento
    * tipo de cliente (personal, empresa, etc).

4. Facturación
* Crear nueva factura:
    - Seleccionar cliente.
    - Agregar múltiples productos con cantidad.
    - Calcular subtotal, IGV (18%), total.
    - Guardar en PDF (usando librerías como reportlab, WeasyPrint o xhtml2pdf).
* Listado de facturas emitidas.
* Detalle de factura.

5. Reportes
-   Ventas por fecha.
-   Facturación por cliente.
-   Productos más vendidos.

6. Configuraciones (opcional)
Personalización de datos de la empresa emisora (nombre, RUC, dirección, etc).

Cambiar logo en facturas.

⚙️ Tecnologías sugeridas:
*   Backend: Flask, Flask-JWT-Extended, Flask-SQLAlchemy
*   Base de datos: SQLite (desarrollo), PostgreSQL/MySQL (producción).
*   Frontend: HTML/CSS con Bootstrap o Vue.js (si quieres SPA).
*   PDF: WeasyPrint o reportlab.
*   Documentación: Flask-RESTX o flasgger para Swagger UI.