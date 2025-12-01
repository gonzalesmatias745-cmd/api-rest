from django.db import models

class Usuario(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.CharField(max_length=150)
    rol = models.CharField(max_length=50)
    contrasena = models.CharField(max_length=255)

    class Meta:
        db_table = 'usuario'


class Rol(models.Model):
    id_roles = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    correo = models.CharField(max_length=100)
    contrasena = models.CharField(max_length=255)
    rol = models.CharField(max_length=20)

    class Meta:
        db_table = 'roles'


class Sensor(models.Model):
    id_sensor = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)

    class Meta:
        db_table = 'sensor'


class LecturaSensor(models.Model):
    id_lectura = models.IntegerField(primary_key=True)
    id_sensor = models.ForeignKey(Sensor, db_column='id_sensor', on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'lectura_sensor'
