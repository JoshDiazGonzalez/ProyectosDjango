from django.shortcuts import render
from django.views.generic import(
    ListView,
    TemplateView,
)

#modelos
from .models import Empleado

# Create your views here.
class ListAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    model = Empleado
