from django.shortcuts import render, redirect, get_list_or_404
from .models import Productos, Usuarios
from .forms 

# Create your views here.
def lista_productos(request):
    productos = Productos.objects.all()
    return render(request, 'productos.html', {'productos': productos})

def crear_producto(request):
    if







def agregar_producto(request):
    if request.method == 'POST':
        form = ProductosForm