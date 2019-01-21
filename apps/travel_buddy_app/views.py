from django.shortcuts import render, redirect
from models import User, Trip
# Create your views here.
def home(request):
    alluser = User.objects.all()
    content = {
        'newuser': alluser
    }
    print("all : ", alluser)
    return render(request,"travel_buddy_app/home.html", content)
    
def create(request):
  
    if request.method == 'POST':
        user_info = request.POST    
        User.objects.register_validation(user_info)
    return redirect('/main')


def login(request):
    return render(request,"travel_buddy_app/home.html")

def travel_dashboard(request):
    return render(request,"travel_buddy_app/dashboard.html")

def add_travel(request):
    return render(request,"travel_buddy_app/add_travel.html")

def destination(request):
    return render(request,"travel_buddy_app/destination.html")
