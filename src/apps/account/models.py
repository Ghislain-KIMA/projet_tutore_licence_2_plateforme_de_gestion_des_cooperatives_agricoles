from django.db import models

class User(models.Model):
    USER_TYPE = [("customer", "Customer"), ("member", "Membre d'une cooperative")]

    user_type = models.CharField(max_length = 10, null = False, choices = USER_TYPE, default = "customer", unique=False)
    user_lastname = models.CharField(max_length = 30, null=False)
    user_firstname = models.CharField(max_length = 60, null=False)
    user_email = models.EmailField(max_length = 100, unique = True)
    user_contact = models.CharField(max_length = 26, unique = True)
    user_home_city = models.CharField(max_length = 100)

class Login(models.Model):
    identity = models.CharField(max_length = 100, null=False)
    password = models.CharField(max_length = 100, null=False)
    last_login = models.DateTimeField(max_length = 30, null = False)
    id_user = models.ForeignKey(User, on_delete = models.CASCADE, null=False)

