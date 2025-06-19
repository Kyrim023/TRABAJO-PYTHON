app_inventario = app
prueba = project

librerias

libreria 1

pip install mysqlclient = esta se toma como la libraria que se escogio para exponer (la original es mysql-conecctor-python, pero como estamos en django, no aplica ya que es unica para python) asi que esta es la conexion de mysql a django

pip install psycopg2 = libreria para postgres
pip install psycopg = libreria para postgres
pip install psycopg2-binary = libreria postgres

libreria 2

pip install pandas = libreria de pandas

pip install django = django

libreria 3

pip install djangorestframework = complemento de django y 3 libreria encargada de la encriptacion de datos a APIs

archivos adicionales:

libreriap.py = en este archivo .py tenemos el uso de la libreria pandas para obtener los registros de las 3 diferentes bases de datos

urls

las urls para probar las bases de datos son:

//////////////// post: 

/inventario/inventario/crear/ = post
/inventario/marca/crear/ = post
/inventario/categoria/crear/ = post
/inventario/estado/crear/ = post

//////////////// get: 

/inventario/inventario/int/ = get
/inventario/marca/int/ = get
/inventario/categoria/int/ = get
/inventario/estado/int/ = get

//////////////// put:

/inventario/inventario/int/editar/ = put
/inventario/marca/int/editar/ = put
/inventario/categoria/int/editar/ = put
/inventario/estado/int/editar/ = put

/////////////// delete:

/inventario/inventario/int/delete/ = delete
/inventario/marca/int/delete/ = delete
/inventario/categoria/int/delete/ = delete
/inventario/estado/int/delete/ = delete

base de datos

- A la base de datos se le llamo "inventario", se da esta informacion ya que es necesario crear una base de datos con anterioridad tanto para mysql como para postgresql
