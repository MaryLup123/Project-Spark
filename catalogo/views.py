# catalogo/views.py
from django.shortcuts import render
from .models import Producto, Categoria

def catalogo(request):
    categoria_id = request.GET.get('categoria')
    categorias = Categoria.objects.all()

    if categoria_id:
        productos = Producto.objects.filter(categoria_id=categoria_id)
    else:
        productos = Producto.objects.all()

    return render(request, 'catalogo/index.html', {
        'productos': productos,
        'categorias': categorias,
    })
