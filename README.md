## Flask App Boilerplate

Cambiar los datos de su base de datos localmente en config.py. 
Si no se conecta muestra el error en el navedador. De lo contrario imprime It works

Configurar el venv y ejecutar 
```
$ export FLASK_DEBUG=1   
$ flask run
```

# Migrations 

Pueden ejecutar migraciones usanfo Flask-Migrate 

Inicia la base de datos
```
$ flask db init
```

Realiza migraciones. Tambien, cada vez que hay un cambio en el esquema hay que ejecutar los dos comandos.
```
$ flask db migrate
```
```
$ flask db upgrade
```

Mas info aca https://github.com/miguelgrinberg/flask-migrate/

# Celery and Rabbit

Para ejecutar los workers de celery correr 
```
$ celery worker -A app.celery --loglevel=info

```



