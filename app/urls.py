from django.urls import path
from .views import cadastrar_tarefa, listar_tarefas

urlpatterns = [
    path('cadastrar_tarefa', cadastrar_tarefa, name='cadastrar_tarefa'),
    path('listar_tarefas', listar_tarefas, name='listar_tarefas'),
]