from django.urls import path
from . import views

urlpatterns=[
    path('',views.loginpage, name='login'),
    path('categorias/',views.home,name="categorias"),
    path('registro/',views.registro,name='registro'),
    path('logout/',views.logoutUser,name='logout'),
    path('categoria/<int:categoria_id>',views.mostrar_categoria,name='mostrar_categoria'),
    path('prestamos/',views.prestamos,name='prestamos')
]