import json
from django.http import JsonResponse, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404, redirect, render
from .models import Aluno

def home(_):
  return redirect("alunos_list_create")

def alunos_list_create(request):
  if request.method == "GET":
    alunos = Aluno.objects.all()
    return render(request, "index.html", { "alunos": alunos })
  
  elif request.method == "POST":
    nome = request.POST.get("aluno_nome")
    email = request.POST.get("aluno_email")

    aluno = Aluno(nome=nome, email=email)
    aluno.save()
    return redirect("alunos_list_create")

def aluno_new(request):
  return render(request, "form.html")

def aluno_edit(request, id):
  aluno = get_object_or_404(Aluno, id=id)
  return render(request, "form.html", {"aluno": aluno})

def aluno_actions(request, id):
  aluno = get_object_or_404(Aluno, id=id)
  method = request.method
  data = {}

  # tenta capturar o corpo (se for JSON)
  if request.content_type == 'application/json':
    try:
      body = request.body.decode('utf-8')
      data = json.loads(body)
    except json.JSONDecodeError:
      data = {}
  else:
    data = request.POST

  if method == "POST":
    method_override = data.get("_method", "").upper()
    if method_override in ["PATCH", "PUT", "DELETE"]:
        method = method_override

  if method in ("PATCH", "PUT"):
    aluno.nome = data.get("aluno_nome", aluno.nome)
    aluno.email = data.get("aluno_email", aluno.email)
    aluno.save()
    return redirect("alunos_list_create")
    

  elif method == "DELETE":
    aluno.delete()
    return redirect("alunos_list_create")
  
  elif method == "GET":
    return render(request, 'show.html', {"aluno": aluno})
  
  else:
    return HttpResponseNotAllowed(["GET", "PATCH", "PUT", "DELETE"])