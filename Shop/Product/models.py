from django.db import models

# Create your models here.
class Product(models.Model):
    nazwa = models.CharField(max_length=100)
    opis = models.TextField(blank=True)
    cena = models.DecimalField(max_digits=12, decimal_places=2)
    def __str__(self):
        return self.nazwa