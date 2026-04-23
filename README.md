# TuPrimeraPagina-GarciaRiveros EMPRESA ROMBO PISOS

## Sobre la empresa
La Empresa Rombo Pisos es una entidad comercial que se dedica a la reventa de baldosas.


## Descripción del proyecto
Este proyecto es una página web desarrollada en Django que permite gestionar proveedores, clientes y baldosas.


## VIDEO
El video se podrá visualizar desde el siguiente link:
https://drive.google.com/drive/folders/1VKZpER1AzVM4cJyLaVICgOzhld-wjMap?usp=sharing

## Funcionalidades

- Registro de usuario (incluye log in, modificación de datos, modificación de password y log out)
- Proveedores (crear, buscar, editar datos, eliminar y vista de reporte)
- Clientes (crear, buscar, editar datos, eliminar y vista de reporte)
- Diseños de baldosas (crear, buscar, editar datos, eliminar y vista de reporte)


## Pasos para acceder a la página web

1. Clonar el repositorio

git clone https://github.com/SolGarcia123/TuPrimeraPagina-GarciaRiveros.git

cd TuPrimeraPagina-GarciaRiveros/empresa

2. Crear un entorno virtual y activarlo

python -m venv env

source env/Scripts/activate

3. Ejecutar el install del archivo requirements.txt

pip install -r requirements.txt

4. Aplicar migraciones

python manage.py makemigrations

python manage.py migrate

5. Ejecutar el servidor

python manage.py runserver

6. Abrir pagina en el navegador

http://127.0.0.1:8000

7. Usar el menú superior para probar las funcionalidades.

## Prueba Diseños (Modelo principal)
1. Ir a la opción "Diseños"->"Añadir Diseño". Ingresar los características del diseño.
2. Ir a la opción "Diseños"->"Buscar Diseño". Buscar por el nombre del diseño.
3. Ir a la opción "Diseños"->"Buscar Diseño". Buscar por el nombre del diseño y presionar el botón "Buscar" y luego, "Editar".
4. Ir a la opción "Diseños"->"Buscar Diseño". Buscar por el nombre del diseño y presionar el botón "Buscar" y luego, "Eliminar".
5. Ir a la opción "Diseños"->"Buscar Diseño". Buscar por el nombre del diseño y presionar el botón "Buscar" y luego, "Ver más detalles".
6. Ir a la opción "Diseños"->"Buscar Diseño". Buscar por el nombre del diseño y presionar el botón "Buscar" y luego, "Reporte".

## Prueba Clientes
1. Ir a la opción "Clientes"->"Añadir cliente". Ingresar los datos del cliente.
2. Ir a la opción "Clientes"->"Buscar Cliente". Buscar por el nombre del cliente.
3. Ir a la opción "Clientes"->"Buscar Cliente". Buscar por el nombre del cliente y presionar el botón "Buscar" y luego, "Editar".
4. Ir a la opción "Clientes"->"Buscar Cliente". Buscar por el nombre del cliente y presionar el botón "Buscar" y luego, "Eliminar".
5. Ir a la opción "Clientes"->"Buscar Cliente". Buscar por el nombre del cliente y presionar el botón "Buscar" y luego, "Ver más detalles".
6. Ir a la opción "Diseños"->"Buscar Cliente". Buscar por el nombre del cliente y presionar el botón "Buscar" y luego, "Reporte".

## Prueba Proveedores
1. Ir a la opción "Proveedores"->"Añadir Proveedor". Ingresar los datos del proveedor.
2. Ir a la opción "Proveedores"->"Buscar Proveedor". Buscar por el nombre del proveedor.
3. Ir a la opción "Proveedores"->"Buscar Proveedor". Buscar por el nombre del proveedor y presionar el botón "Buscar" y luego, "Editar".
4. Ir a la opción "Proveedores"->"Buscar Proveedor". Buscar por el nombre del proveedor y presionar el botón "Buscar" y luego, "Eliminar".
5. Ir a la opción "Proveedores"->"Buscar Proveedor". Buscar por el nombre del proveedor y presionar el botón "Buscar" y luego, "Ver más detalles".
6. Ir a la opción "Proveedores"->"Buscar Proveedor". Buscar por el nombre del proveedor y presionar el botón "Buscar" y luego, "Reporte".

## Prueba Usuario
1. Ir a la opción "Inicio". Página Principal, contacto y redes sociales.
2. Ir a la opción "Inicio"-> "About Us". Información de la empresa y desarrollador de la página web.
3. Ir a la opción "Inicio"->"Registrarse". Crear un usuario.
4. Ir a la opción "Inicio"->"Iniciar Sesión". Realizar login.
5. Ir a la opción "Inicio"->"Iniciar Sesión" -> "Perfil". Cambiar datos del perfil.
6. Ir a la opción "Inicio"->"Iniciar Sesión" -> "Perfil"->"Cambiar Contraseña". Cambiar contraseña del perfil.
7. Ir a la opción "Inicio"->"Cerrar Sesión". Realizar logout.

## Tecnologías usadas
- Python
- Django
- HTML + CSS
- Material y clases en vivo de CoderHouse
