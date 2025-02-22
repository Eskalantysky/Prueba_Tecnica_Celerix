# Prueba Técnica Celerix

Este repositorio contiene dos carpetas denominadas `Parte1` y `Parte2`, además de un archivo `.gitignore` y un `README.md`.

Para la implementación de este programa se debe tener instalado un `Docker Desktop`, tener instalado `GIT` o `GIT bash`, y una versión de `Python 3.10` o superior.

## Clonación del Repositorio

Para comenzar, abra una consola o terminal con `Git`. Ubíquese en la ruta donde desea descargar el repositorio y ejecute el siguiente comando:

<pre>git clone https://github.com/Eskalantysky/Prueba_Tecnica_Celerix.git</pre>

## Configuración del Entorno Virtual en Python

Una vez clonado el repositorio, acceda a la carpeta `Parte2` desde la terminal y cree un entorno virtual de Python con el siguiente comando:

<pre>python -m venv .venv</pre>

Para activar el entorno virtual, ejecute:

<pre>./.venv/Scripts/activate</pre>

Asegúrese de actualizar `pip` en el entorno virtual:

<pre>python -m pip install --upgrade pip</pre>

Instale las librerías necesarias con el siguiente comando:

<pre>pip install pandas psycopg2 sqlalchemy python-dotenv</pre>

## Despliegue con Docker

Para desplegar los servicios, asegúrese de que la terminal esté ubicada en la carpeta `Parte2` y ejecute el siguiente comando:

<pre>docker-compose up --build</pre>

## Acceso a PostgreSQL dentro del Contenedor

Una vez finalizado el despliegue, abra una nueva terminal `PowerShell`, ubíquese en la carpeta `Parte2` y acceda a `psql` dentro del contenedor ejecutando el siguiente comando:

<pre>docker compose exec db psql -U user -d etl_db</pre>

Este comando permite conectarse a la base de datos PostgreSQL dentro del contenedor para realizar consultas y verificar la correcta carga de datos.

Se le mostrará una nueva terminal esperando indicaciones como 
<pre>etl_db #</pre>

En aquella terminal espera que le de instrucción para algun consulta.
Quiero aclarar que desde el etl.py la tabla creada se llama `tabla_principal`, por lo tanto se puede hacer una consulta de SQL como por ejemplo:
<pre>SELECT * FROM tabla_principal LIMIT 10;</pre> 

Una vez que ingrese la consulta, se puede decir que el servidor está funcionando adecuadamente.
Para salir de la terminal solo escribe:
<pre>\q</pre>


## Comando Auxiliares
docker compose down -v  # Elimina los contenedores y volúmenes asociados
docker system prune -a  # Elimina todas las imágenes y contenedores detenidos
docker ps -a            # Lista todos los contenedores
