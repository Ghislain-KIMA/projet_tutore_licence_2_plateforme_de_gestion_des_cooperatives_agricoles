from django.db import models

from apps.account.models import User
from apps.member.models import Product

class Command(models.Model):
    command_quotation = models.FloatField(null=False)

class Cmd_Contain(models.Model):
    product_qty = models.FloatField(null=False)
    id_command = models.ForeignKey(Command, on_delete=models.SET_NULL, null=True)
    id_product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)

class Payment(models.Model):
    payment_operator = models.CharField(max_length=60, null=False)
    payment_amount = models.FloatField(null=False)

class Order_Cmd(models.Model):
    date_payment = models.DateField(max_length=10, null=False, unique=False)
    id_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, unique=False)
    id_command = models.ForeignKey(Command, on_delete=models.SET_NULL, null=True, unique=True)
    id_payment = models.ForeignKey(Payment, on_delete=models.SET_NULL, null=True, unique=True)