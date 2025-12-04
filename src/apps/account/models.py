from django.db import models

from apps.customer.models import User

class Login(models.Model):
    identity = models.CharField(max_length = 100, null=False)
    password = models.CharField(max_length = 100, null=False)
    last_login = models.DateTimeField(max_length = 30, null = False)
    id_user = models.ForeignKey(User, on_delete = models.CASCADE, null=False)
