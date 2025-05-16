# catalogo/views.py
from django.shortcuts import render
from .models import Producto, Categoria

def catalogo(request):
    categorias = Categoria.objects.all()
    productos = Producto.objects.all()
    categoria_filter = request.GET.get('categoria', None)

    if categoria_filter:
        productos = productos.filter(categoria__id=categoria_filter)

    return render(request, 'catalogo/index.html', {
        'productos': productos,
        'categorias': categorias
    })
