# mi_proyecto/mi_app/models.py

from django.db import models

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=100)
    is_deleted = models.IntegerField(default=0)  # Ajustar a IntegerField si `is_deleted` es un entero

    def __str__(self):
        return self.category_name

# Create your models here.
