# Alejandria

### Primeros pasos

Una vez bajado el proyecto teneis que crear un virtual environment e instalar los requirements con:
```
pip install -r requirements.txt 
```
usando el requirements.txt que ya tiene el proyecto.

### Configuración de la DB

- Para configurar la DB necesitareis instalar PostgresSQL en el siguiente [enlace](https://www.postgresql.org/download/) (Preferiblemente descargad la version 12, en caso contrario la 11).

- Una vez se ha instalado el PostgresSQL debeis aseguraros de que habeis instalado los requirements y que entre ellos teneis la libreria `psycopg2` instalada en el environment.

- Accedeis al pgAdmin con la contraseña puesta en la instalación.

- En pgAdmin accedeis a `Login/Group Roles` y creais un nuevo usuario `Alejandro` con contraseña `Password1` al que le assignais todos los permisos posibles, una fecha de expiración lejana y le dais de Membership 'postgres' si es posible.

- Creais la database con nombre `Alejandria_DB` y le asignais de de Owner `Alejandro`.

- En el root del proyecto (donde se encuentra el archivo `manage.py`) ejecutais los siguientes comandos `python manage.py makemigrations` y `python manage.py migrate`. Si todo lo habeis hecho bien os debería estar saliendo por consola unos mensajes Applying...OK donde se generan las tablas de base de datos por defecto de django.

- Por último comprobad en el pgAdmin (haced un refresh de la DB) si las tablas se han generado correctamente. Para ello acceded a la base de datos `Alejandria_DB->Schemas->Public->Tables` y alli encontrareis las tablas de nuestra base de datos.



### Configuración Testing 

Vamos a utilizar la librería ``pytest`` para la creación y comprobación de nuestros test. Para ello:

- Instalamos la librería mediante  el `pip install -r requirements.txt`.(En caso de no funcionar , ejecutar `pip install pytest`).

- Usando PyCharm su integración es muy simple. Nos dirigimos a `Settings/Preferences | Tools | Python Integrated Tool` y seleccionamos como `Default test runner` nuestro `pytest`. (En caso de no detectar aún pytest, reiniciar el IDE).

- Ahora para crear cualquier test solo debemos posicionarnos sobre la clase o función a testear, click `secundario` y seleccionar `Go To | Test` , nos dará ahora la opción `Create a new Test`.

- Mover todos los ficheros `test_*.py` a la carpeta `test`.

- Los test deben seguir la estructura marcada por [este ejemplo](./books/test/test_models.py).

- Para ejecutar los test le damos a la propia ejecución desde el fichero de test (saldrá un icono de ejecutar en la linea de definición de la función) o bien si queremos ejecutar manualmente por consola `pytest archivo_de_test.py` o `pytest archivo_de_test.py::funcion_a_testear` o `pytest archivo_de_test.py::Clase::funcion_a_testear`

- Por último comprobar que el estado de la ejecución es PASSED.