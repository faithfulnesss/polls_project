from django.shortcuts import render, redirect

from app.models import Poll, User

from django.contrib.auth import logout, login, authenticate

from django.contrib.auth.decorators import login_required

from django.contrib import messages

# Create your views here.
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Wrong username or password!")
            return redirect('login')
    else:
        return render(request, "login.html", {})

def index_view(request):
    return render(request, "index.html", {})

def register_view(request):
    if request.method == "POST":
        try:
            user = User.objects.get(username=request.POST['username'])
            messages.error(request, "Username is already taken!")
            return redirect('register')

        except User.DoesNotExist:
            if(request.POST['password'] == request.POST['confirm_password']):
                user = User.objects.create_user(request.POST['username'], password = request.POST['password'])
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, "Passwords are not the same!")
                return redirect('register')
    else:
        return render(request, "register.html", {})

@login_required(login_url="/login")
def create_view(request):
    return render(request, "index.html", {})
    
@login_required(login_url="/login")
def profile_view(request):
    return render(request, "index.html")

@login_required(login_url="/login")
def logout_view(request):
    logout(request)
    return redirect("index")


