from django.shortcuts import render, redirect
from models import User, Trip
# Create your views here.
def home(request):
    return render(request,"travel_buddy_app/home.html")
    
def create(request):
    if request.method == 'POST':
        print(" You have just created a new user " + request)
        User.objects.register_validation(request)
    return redirect('/main')


def travel_dashboard(request):
    return render(request,"travel_buddy_app/dashboard.html")

def add_travel(request):
    return render(request,"travel_buddy_app/add_travel.html")

def destination(request):
    return render(request,"travel_buddy_app/destination.html")
