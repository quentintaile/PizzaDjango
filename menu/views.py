from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza

# Create your views here.

def index(request):
    pizzas = Pizza.objects.all()
    Pizzas_name = [pizza.nom for pizza in pizzas]
    pizzas_names_str = ",".join(Pizzas_name)
    return HttpResponse("Les Pizzas : " + pizzas_names_str)