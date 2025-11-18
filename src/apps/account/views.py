from django.shortcuts import render, redirect
from .forms import Login_Form
from .models import Login
from pgca.views import index

def index(request):
    if request.method == "POST" :
        form = Login_Form(request.POST)
        if form.is_valid() :
            identity = form.cleaned_data["identity"]
            password = form.cleaned_data["password"]
            try :
                login = Login.objects.get(identity=identity, password=password)
                if (login.identity == identity) and (login.password == password) :
                    return redirect("index")
                else :
                    print("Connexion non réussit")
            except :
                print("Problème de saisie")
    else :
        form = Login_Form()
    return render(request, "account/index.html", context={"form":form})
