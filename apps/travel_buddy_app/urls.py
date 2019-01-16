from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^main$', views.home),
    url(r'^travels$',views.travel_dashboard),
    url(r'^travels/add$',views.add_travel),
    url(r'^destination$',views.destination),
]
