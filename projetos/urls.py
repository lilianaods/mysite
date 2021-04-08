from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('listar/', views.listar, name='listar'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('<int:projeto_id>/editar/', views.editar, name='editar'),
]
