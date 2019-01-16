from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"travel_buddy_app/home.html")

def travel_dashboard(request):
    return render(request,"travel_buddy_app/dashboard.html")

def add_travel(request):
    return render(request,"travel_buddy_app/add_travel.html")

def destination(request):
    return render(request,"travel_buddy_app/destination.html")
