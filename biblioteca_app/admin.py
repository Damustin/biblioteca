from django.contrib import admin

# Register your models here.
from .models import Categoria,Libro,Prestamo,Autor

admin.site.register(Categoria)
admin.site.register(Autor)
admin.site.register(Libro)
admin.site.register(Prestamo)