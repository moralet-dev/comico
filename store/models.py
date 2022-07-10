from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=2000, null=True, blank=True)
    price = models.DecimalField(max_length=7, decimal_places=2)


