from django.db import models

# Create your models here.

# Creando Tablas de Clientes
class Clientes(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50, verbose_name="Dirección Electronico") # verbose => name campo que aparece en panel de administracion
    email = models.EmailField(blank=True, null=True) # el campo es opcional
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre

# Creando Tablas de Articulos
class Articulos(models.Model):
    nombre = models.CharField(max_length=30)
    seccion = models.CharField(max_length=20)
    precio = models.IntegerField()

    def __str__(self):
        return 'El nombre es %s la sección es %s y el precio es %s' % (self.nombre, self.seccion, self.precio)

# Creando Tabla de Pedidos
class Pedidos(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()