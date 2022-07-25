from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from Accounts.forms import UserRegisterForm, UserEditForm
from django.contrib.auth.decorators import login_required
from Accounts.models import User

# Create your views here.

def login_request(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contraseña = form.cleaned_data.get("password")

            user = authenticate(username=usuario, password=contraseña)


            if user is not None:
                login(request,user)

                return render(request,"Blog/inicio2.html", {"mensaje":f"Welcome {usuario}"})
            else:
                
                return render(request,"Blog/inicio.html", {"mensaje":"Log In failed, wrong data"})
            
        else:

                return render(request,"Accounts/loginmalo.html", {"mensaje":"Error, wrong form"})
    
    form = AuthenticationForm()

    return render(request, "Accounts/login.html", {"form":form})

def signup(request):

    if request.method == "POST":

        form = UserRegisterForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data["username"]
            form.save()
            return render(request,"Blog/inicio.html", {"mensaje":"User Created"})

    else:
        form = UserRegisterForm()

    return render(request,"Accounts/signup.html", {"form":form})

def updateProfile(request):

    usuario = request.user

    if request.method == "POST":
        myForm = UserEditForm(request.POST)
        if myForm.is_valid:

            return render(request, "Accounts/profileupdated.html")
    
    else:

        myForm = UserEditForm(initial={"email":usuario.email})
    
    return render(request, "Accounts/updateprofile.html", {"myForm":myForm, "usuario":usuario})
