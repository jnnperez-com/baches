from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Reporte(models.Model):
	image = models.ImageField(upload_to = 'image', verbose_name = 'Imagén' )
	name = models.CharField(max_length=140, verbose_name = 'nome',)
	owner = models.ForeignKey(User, verbose_name='usuario')
	date = models.DateTimeField(auto_now_add = True, verbose_name='Creacion')
	place = models.CharField(blank=True, max_length=50)


	def __str__(self):
		return self.name
