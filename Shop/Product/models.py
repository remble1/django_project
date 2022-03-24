from django.db import models

class Category(models.Model):
    def __str__(self):
        return self.nazwa
    nazwa = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

# Create your models here.
class Producent(models.Model):
    def __str__(self):
        return self.nazwa

    nazwa = models.CharField(max_length=60)
    opis = models.TextField(blank=True)

class Product(models.Model):
    def __str__(self):
        return self.nazwa # obj Product return name

    kategoria = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    producent = models.ForeignKey(Producent, on_delete=models.CASCADE, null=True)
    nazwa = models.CharField(max_length=100)
    opis = models.TextField(blank=True)
    cena = models.DecimalField(max_digits=12, decimal_places=2)


