from django.urls import path
from . import views

urlpatterns = [
  path("", views.home, name="home"),
  path('alunos/', views.alunos_list_create, name="alunos_list_create"),
  path('alunos/new/', views.aluno_new, name="novo_aluno"),
  path('alunos/<int:id>', views.aluno_actions, name="aluno_actions"),
  path('alunos/<int:id>/edit/', views.aluno_edit, name="editar_aluno"),
]