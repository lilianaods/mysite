from django.shortcuts import get_object_or_404, render, redirect
from .models import Projeto

from datetime import datetime

def index(request):
    return render(request, 'projetos/index.html')

def listar(request):
    lista_projeto = Projeto.objects.all()

    context = {
        'lista_projeto': lista_projeto,
    }

    return render(request, 'projetos/listar.html', context)

def editar(request, projeto_id):
    projeto = get_object_or_404(Projeto, pk=projeto_id)
    return render(request, 'projetos/editar.html', {'projeto': projeto})

def cadastrar(request):
    if request.method == 'GET':
        return render(request, 'projetos/cadastrar.html')
    elif request.method == 'POST':
        data = request.POST.dict()

        nome = data['nome']
        data_de_inicio = datetime.strptime(data['data_de_inicio'], '%Y-%m-%d')
        data_de_termino = datetime.strptime(data['data_de_termino'], '%Y-%m-%d')
        valor = data['valor']
        risco = data['risco']

        projeto = Projeto(nome=nome, data_de_inicio=data_de_inicio, data_de_termino=data_de_termino, valor=valor, risco=risco)
        projeto.save()

        return redirect('listar')
