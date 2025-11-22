from django.db import models

from apps.account.models import User
# from apps.customer.models import Statement, Command

class Product(models.Model):
    product_name = models.CharField(max_length=60, null=False)
    product_unity_price = models.FloatField(null=False)

class Inject_Prod(models.Model):
    product_qty = models.FloatField(null=False)
    id_product = models.ForeignKey(Product, on_delete=models.PROTECT, null=False)
    id_user = models.ForeignKey(User, on_delete=models.PROTECT, null=False)

class Member_Function(models.Model):
    type_function = models.CharField(max_length=30, primary_key=True, null=False, unique=True)
    description = models.CharField(max_length=300, null=False)

class Having_Function(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    type_function = models.ForeignKey(Member_Function, on_delete=models.CASCADE, null=False)

class Module_Formation(models.Model):
    m_formation_name = models.CharField(max_length=100, null=False)
    m_formation_desc = models.CharField(max_length=300, null=False)

class Waching(models.Model):
    waching_date = models.DateTimeField(null=False)
    waching_nb = models.IntegerField(default=0, null=False)
    id_m_formation = models.ForeignKey(Module_Formation, on_delete=models.PROTECT, null=False)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

class Delivery(models.Model):
    delivery_person = models.CharField(max_length=90, null=False)
    delivery_sender = models.CharField(max_length=90, null=False)

class Render_up(models.Model):
    render_up_date = models.DateTimeField(max_length=30, null=False)
    id_statement = models.ForeignKey("customer.Statement", on_delete=models.CASCADE, null=False)
    id_delivery = models.ForeignKey(Delivery, on_delete=models.PROTECT, null=False)
    id_command = models.ForeignKey("customer.Command", on_delete=models.PROTECT, null=False)
    id_user = models.ForeignKey(User, on_delete=models.PROTECT, null=False)