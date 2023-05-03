## Creación de projecto en Python con django con administradores automaticos

En este tutorial vamos a crear un proyecto en python usando el framework django para la creación de administradores automáticos

- Descargue  e instale ptython en https://www.python.org/downloads/, si ya lo instalado omitir este paso

- Abra la carpeta creada en visual studio code y inicie la ejecución de comandos

- Todos los comandos de terminal que se ejecutan en adelante será en una terminal de CMD (Command Prompt), usaremos visual estudio code y la terminal integrada

## Configuración entorno virtual

- Instalamos venv para la creación de entorno virtual.  "myvenv" es mi entonro virtual

```console
py -m venv myvenv
```

- Activamos el entorno virual creado
```console
myvenv\Scripts\activate
```

## Instalación django

- Instalamos django
```console
py -m pip install Django
```

- Creamos el proyecto llamado "project"
```console
django-admin startproject project
```

- Accedemos a nuestro proyecto "cd project"
```console
cd project
```
- Ejecutamos proyecto para validar su ejecución.

```console
py manage.py runserver
```
Accedemos a http://127.0.0.1:8000 para validar que el proyecto esté corriendo correctamente


## Base de datos
- Instalación de mysql (o motor de base de datos usar): Realizamos la instalación de mysql, puede ser con xampp u otro programa, para instalar xampp puede acceder a la url https://www.apachefriends.org/es/index.html

- Creación de Base de datos: Creamos la base de datos que vamos a utilizar en nuestro proyecto


- Instalación de modulo de cliente de mysql para python (ctrl+c para finalizar la ejecución)

```console
py -m pip install mysqlclient
```

- Configuramos base de datos: Configuramos la conexión a la base de datos en el archivo de settings.py ubicado en project/settings.py. El parametro ENGINE indica el proveedor de base de datos que vamos a usar, en este caso es mysql (django.db.backends.mysql)
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nombre_bd',
        'USER': 'usuario_bd',
        'PASSWORD': 'clave_bd',
        'HOST': 'host_bd',
        'PORT': '3306',
    }
}
```

- Ejecutamos migración

``` console
    py manage.py migrate
```

- Al ejecutar el comando anterior creará en la base de datos la todas las tablas necesarios para al funcionamiento del administrador de django.  Nos motrará en consola la siguente salida con todas las migraciones ejecutadas
``` console
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions, tarea
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
```

## Nueva App de tareas
-  Ejecutamos comando para la creación de la nueva app (o modulo) tarea que tendrá las funcionalidades de tareas.
```console
- py manage.py startapp tarea
```

- Agreagr a app de a nuestro projecto, modificando la variable INSTALLED_APPS en project/settings.py. Se agrega el nombre de la nueva app de tarea
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tarea'  #agregando nueva app
]
```

- Creamos del modelo, configuramos le modelo en el archivo tarea/models.py

```python
class Tarea(models.Model):
    nombre = models.CharField("nombre", max_length=50)
    fecha = models.DateField("fecha", auto_now=False, auto_now_add=False)
    descripcion = models.CharField("descripcion", max_length=50)
    finalizada = models.BooleanField("finalizada")
    created_at = models.DateTimeField("create_at", auto_now_add=True)
    updated_at = models.DateTimeField("update_at", auto_now=True) 

    class Meta:
        db_table = 'tareas'
```

## Migraciones

- Generar migraciones
```console
py manage.py makemigrations
```
- Muestra las migraciones encotnradas
```console
Migrations for 'tarea':
  tarea\migrations\0001_initial.py
    - Create model Tareas
```
- Ejecutar migraciones encotnradas
```console
py manage.py migrate
```
- Ejecuta las migraciones en la base de datos
```console
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions, tarea
Running migrations:
  Applying tarea.0001_initial... OK
```
<p>Validamos la creación en la base de datos<p>

## Configuramos administrador de nuevo modelo (tarea)

- Configuramos en tarea/admin.py
```python

#importar modelo
from .models import Tarea

#configuración administrador de modelo
@admin.register(Tarea)
class TareasAdmin(admin.ModelAdmin):
    """Tareas admin."""
    list_display = ('id', 'nombre', 'fecha', 'descripcion', 'finalizada')

```

## Create user admin
- Ejecutamos comando de creación de super usuario
```console
py manage.py createsuperuser
```
- Se ejecuta asistente que nos va pidiendo uno a uno los datos del usuario
```console
    Username (leave blank to use 'user'): admin
    Email address: admin@gmail.com
    Password:
    Password (again):
    This password is too short. It must contain at least 8 characters.
    This password is too common.
    This password is entirely numeric.
    Bypass password validation and create user anyway? [y/N]: y
    Superuser created successfully. 
```

- Ejecutamos proyecto para validar su ejecución.

```console
py manage.py runserver
```

- Revisamos funcionalidades del administrador accediendo a http://127.0.0.1:8000/admin/login, para acceder usamos las credenciales de super usuario que creamos


