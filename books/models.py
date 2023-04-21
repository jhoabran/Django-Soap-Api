from djongo import models

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, blank=False, default='')
    descripcion = models.TextField( blank=False, default='')
    