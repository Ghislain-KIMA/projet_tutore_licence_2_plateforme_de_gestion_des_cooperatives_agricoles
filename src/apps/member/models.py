from django.db import models

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=60, null=False)
    product_unity_price = models.FloatField(null=False)