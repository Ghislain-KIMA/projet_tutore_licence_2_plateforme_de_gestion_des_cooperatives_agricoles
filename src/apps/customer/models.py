from django.db import models

class User(models.Model):
    USER_TYPE = [("client", "Customer"), ("membre", "Membre d'une cooperative")]

    user_type = models.CharField(max_length = 10, null = False, choices = USER_TYPE, default = "client", unique=False)
    user_lastname = models.CharField(max_length = 30, null=False)
    user_firstname = models.CharField(max_length = 60, null=False)
    user_email = models.EmailField(max_length = 100, unique = True)
    user_contact = models.CharField(max_length = 26, unique = True)
    user_home_city = models.CharField(max_length = 100)

class Command(models.Model):
    command_quotation = models.FloatField(null=False)

class Cmd_Contain(models.Model):
    product_qty = models.FloatField(null=False)
    id_command = models.ForeignKey(Command, on_delete=models.SET_NULL, null=True)
    id_product = models.ForeignKey("member.Product", on_delete=models.SET_NULL, null=True)

class Payment(models.Model):
    payment_operator = models.CharField(max_length=60, null=False)
    payment_amount = models.FloatField(null=False)

class Order_Cmd(models.Model):
    date_payment = models.DateTimeField(max_length=10, null=False, unique=False)
    id_user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    id_command = models.OneToOneField(Command, on_delete=models.SET_NULL, null=True)
    id_payment = models.OneToOneField(Payment, on_delete=models.SET_NULL, null=True)

class Statement(models.Model):
    statement_tax = models.FloatField(null=False)