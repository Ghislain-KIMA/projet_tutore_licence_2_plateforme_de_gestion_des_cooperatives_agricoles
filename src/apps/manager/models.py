from django.db import models

from apps.member.models import Product
from apps.member.models import Delivery

class Store(models.Model):
    store_home_city = models.CharField(max_length=30, null=False)

class Storage(models.Model):
    product_qty = models.FloatField(null=False, default=0.0)
    id_store = models.ForeignKey(Store, on_delete=models.CASCADE, null=False)
    id_product = models.ForeignKey(Product, on_delete=models.PROTECT, null=False)

class Debiting(models.Model):
    product_qty = models.CharField(null=False)
    debiting_date = models.DateTimeField(max_length=30, null=False)
    id_product = models.ForeignKey(Product, on_delete=models.PROTECT, null=False)
    id_store = models.ForeignKey(Store, on_delete=models.PROTECT, null=False)
    id_delivery = models.ForeignKey(Delivery, on_delete=models.PROTECT, null=False)