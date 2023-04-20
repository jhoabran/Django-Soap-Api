from djongo import models

class Book(models.Model):
    nombre = models.CharField(max_length=100, blank=False, default='')
    descripcion = models.CharField(max_length=300, blank=False, default='')
    