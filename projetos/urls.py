from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('listar/', views.listar, name='listar'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('<int:projeto_id>/editar/', views.editar, name='editar'),
    path('<int:projeto_id>/excluir/', views.excluir, name='excluir'),
    path('participante/cadastrar/', views.participante_cadastrar, name='participante_cadastrar'),
]
