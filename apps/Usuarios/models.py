# coding: utf8
from __future__ import unicode_literals
from django.core.validators import RegexValidator
from django.utils import timezone
from django.db import models
from geoposition.fields import GeopositionField
from tagging.fields import TagField
from tagging.models import Tag
# Create your models here.
class Users(models.Model):
    name = models.CharField('Nombre',max_length=200)
    birth_date = models.DateTimeField('Fecha de nacimiento')
    created = models.DateTimeField('Creado',default = timezone.now, editable = False)
    address = GeopositionField('Direccion')
    age = models.IntegerField('Edad')
    specialities = TagField('Especialidades')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Número telefónico debe estar en el formato: '+999999999'. Hasta 15 dígitos permitidos.")
    #phone = models.CharField('Teléfono', max_length = 17, validators=[phone_regex], blank=True) # validators should be a list
    email = models.EmailField('Correo electronico', blank = True)

    def distancia(self,lat,lng):
    	pass

    def __str__(self):
        return '%s, especialidades = %s' % (self.name, self.specialities)

    class Meta:
    	get_latest_by = "created"
    		

    def get_tags(self):
        return Tag.objects.get_for_object(self)

        #Falta un modelo para reseñas
        #Falta un modelo de Usuarios de verdad