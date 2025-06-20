from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')
\
def addrecipe(request):
    return render(request, 'addrecipe.html')

def feedback(request):
    return render(request, 'feedback.html')

def recipes(request):
    return render(request, 'recipes.html')