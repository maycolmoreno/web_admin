
from __future__ import unicode_literals
from django.conf import settings
from django.core.validators import MaxValueValidator

from django.db import models

from django.db import models
class Persona(models.Model):
    id_persona = models.AutoField(primary_key=True)
    cedula = models.CharField(max_length = 15, unique=True,verbose_name= "Cedula Identidad")
    nombre = models.CharField(max_length = 50,verbose_name= "Nombre")
    apellido = models.CharField(max_length = 50,verbose_name= "Apellido")
    direccion = models.CharField(max_length = 200,verbose_name= "direccion")
    telefono = models.CharField(max_length = 15,verbose_name= "telefono")
    barrio= models.CharField(max_length = 2000, blank = False, null= False, verbose_name= "Barrio")
    e_civil= models.CharField(max_length = 2000, blank = False, null= False, verbose_name= "Estado Civil")
    f_nac= models.DateField()
    estado = models.BooleanField()
    genero = models.BooleanField()
    user = models.OneToOneField(settings.AUTH_USER_MODEL)   
    def __str__(self):
        return self.nombre
    
class Celulas(models.Model):
    codigo= models.AutoField(primary_key= True)
    persona = models.ForeignKey('Persona')
    nomcelula= models.CharField(max_length = 2000, blank = False, null= False, verbose_name= "nombre")
    barrio= models.CharField(max_length = 2000, blank = False, null= False)
    diacelula= models.CharField(max_length = 2000, blank = False, null= False)
    lugar= models.CharField(max_length = 2000, blank = False, null= False)
    estado_celula = models.BooleanField()
    persona = models.ForeignKey('Persona')
    
    def __str__(self):
        return self.nomcelula
# Create your models here.

class Servicio(models.Model):
 	"""docstring for Servicio"""
 	id_servicio = models.AutoField(primary_key=True)
 	nombre = models.CharField(max_length = 40)
 	precio = models.DecimalField(max_digits=7, decimal_places=2)
 	estado = models.BooleanField()
  
        def __str__(self):
            return self.nombre

class Registrado(models.Model):
	nombre = models.CharField(max_length=100, blank=True, null=True)
	email = models.EmailField()
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

        def __str__(self):
            return self.email

class Galeria(models.Model):
	"""docstring for Galeria"""
	
	id_galeria = models.AutoField(primary_key=True)
	imagen = models.ImageField(upload_to = 'galeria', null=False, blank=False)
	nombre_imagen = models.CharField(max_length = 100)

        def __str__(self):
            return self.nombre_imagen
