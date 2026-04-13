# TuPrimeraPagina-GarciaRiveros EMPRESA ROMBO PISOS

## Sobre la empresa
La Empresa Rombo Pisos es una entidad comercial que se dedica a la reventa de baldosas.


## Descripción del projecto
Este proyecto es una página web desarrollada en Django que permite gestionar proveedores, clientes y baldosas.

## Funcionalidades

- Registro de usuario(incluye log in, modificación del perfil y log out)
- Añadir proveedores (persona/empresa que venden el producto final)
- Añadir clientes (personas que compraron el producto)
- Añadir nuevos diseños de baldosas
- Buscar clientes
- Buscar diseños de baldosas existentes

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

7. Usar el menú superior para probar las funcionalidades:
- Cargar datos (clientes, proveedores, baldosas)
- Buscar información (clientes, baldosas)

## Prueba Clientes
1. Ir a la opción "Cliente" --> Ingresar los datos del cliente --> Por ejemplo: Maximiliano maxi@gmail.com
2. Ir a la opción "Buscar Cliente" --> Buscar por el nombre del cliente --> Por ejemplo: Maximiliano

## Prueba Proveedores
1. Ir a la opción "Proveedor" --> Ingresar los datos del proveedor --> Por ejemplo: Proveedor MAX 1156986236
2. Ingresar un modelo de baldosa y asociarle un proveedor --> Por ejemplo: #001 Negro 1200 Proveedor MAX

## Prueba Baldosas
1. Ir a la opción "Baldosa" --> Ingresar los datos del nuevo modelo de baldosa --> Por ejemplo: #001 Negro 1200 Proveedor MAX
2. Ir a la opción "Buscar Baldosa" --> Buscar por el codigo de la baldosa --> Por ejemplo: #001

## Tecnologías usadas

- Python
- Django
- HTML + CSS
- Material y clases en vivo de CoderHouse
