from django import forms
from .models import Login

class Login_Form(forms.ModelForm):
    class Meta:
        model = Login
        fields = ["identity", "password"]
        widgets = {
            "password": forms.PasswordInput()
        }


    