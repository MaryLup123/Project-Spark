# catalogo/urls.py

from django.urls import path
from . import views


urlpatterns = [
    path('', views.catalogo, name='catalogo'),  # Ruta para mostrar los productos
]
