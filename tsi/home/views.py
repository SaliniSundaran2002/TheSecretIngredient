from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'signup.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return render(request, 'signup.html')

        user = User.objects.create_user(username=username, password=password)
        user.save()
        messages.success(request, "Account created successfully. Please log in.")
        return redirect("{% url 'login' %}")

    return render(request, 'signup.html')

def addrecipe(request):
    return render(request, 'addrecipe.html')

def feedback(request):
    return render(request, 'feedback.html')

def recipes(request):
    return render(request, 'recipes.html')
def footer(request):
    return render(request, 'footer.html')