from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import (
    PessoaForm, 
    VeiculoForm, 
    MovRotativoForm, 
    MensalistaForm,
    MovMensalistaForm,
)
from .models import (
    Pessoa, 
    Veiculo, 
    MovRotativo, 
    Mensalista, 
    MovMensalista,    
)

def home(request):
    context = {'mensagem': 'Ola novamente'}
    return render(request, 'core/index.html', context)

# OS METODOS ABAIXO RETORNA PESSOA/ATUALIZA/DELETA

def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    forms = PessoaForm()
    data = {'pessoas': pessoas, 'forms': forms} 
    return render(request, 'core/lista_pessoas.html', data)

def pessoas_novas(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_pessoas')

def pessoa_update(request, id):
    data = {}
    pessoa = Pessoa.objects.get(id=id)
    form = PessoaForm(request.POST or None, instance=pessoa)
    data['pessoa'] = pessoa
    data['form'] = form

    if request.method == 'POST' and form.is_valid():
        #if form.is_valid():
            form.save()
            return redirect('core_lista_pessoas')
    else:
        return render(request, 'core/pessoa_update.html', data)

def pessoa_delete(request, id):
    pessoa = Pessoa.objects.get(id=id)
    if request.method == 'POST':
        pessoa.delete()
        return redirect('core_lista_pessoas')
    else:
        return render(request, 'core/pessoaconfirme_delete.html', {'pessoa': pessoa})
# OS METODOS ABAIXO RETORNA VEICULOS/ATUALIZA/DELETA


def lista_veiculos(request):    
    veiculos = Veiculo.objects.all()
    forms = VeiculoForm()
    data =  {'veiculo': veiculos, 'forms': forms}
    return render(request, 'core/lista_veiculos.html', data)

def novo_veiculo(request):
    form = VeiculoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_veiculos')

def veiculo_update(request, id):
    data = {}
    veiculo = Veiculo.objects.get(id=id)
    form = VeiculoForm(request.POST or None, instance=veiculo) 
    data['veiculo'] = veiculo
    data['form'] = form

    if request.method == 'POST':
        form.save()
        return redirect('core_lista_veiculos') 
    else:
        return render(request, 'core/veiculo_update.html', data)

def veiculo_delete(request, id):
    veiculo = Veiculo.objects.get(id=id)
    if request.method == 'POST':
        veiculo.delete()
        return redirect('core_lista_veiculos')
    else:
        return render(request, 'core/veiculoconfirme_delete.html', {'veiculo': veiculo})

# OS METODOS ABAIXO RETORNA OS MOVIMENTOS ROTATIVOS/ATUALIZA/CADASTRA/DELETA


def lista_movrotativo(request):
    movimentos = MovRotativo.objects.all()
    forms = MovRotativoForm()
    data =  {'movimentos': movimentos, 'forms': forms}
    return render(request, 'core/lista_movrotativo.html', data)

def novo_rotativo(request):
    form = MovRotativoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_movrotativos')

def movrotativo_update(request, id):
    data = {}
    movrotativo = MovRotativo.objects.get(id=id)
    form = MovRotativoForm(request.POST or None, instance=movrotativo) 
    data['movrotativo'] = movrotativo
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
           form.save()
           return redirect('core_lista_movrotativos') 
    else:
        return render(request, 'core/movrotativo_update.html', data)

def movrotativo_delete(request, id):
    movrotativo = MovRotativo.objects.get(id=id)
    if request.method == 'POST':
        movrotativo.delete()
        return redirect('core_lista_movrotativos')
    else:
        return render(request, 'core/mvrotconfirme_delete.html', {'movrotativo': movrotativo})


# OS METODOS ABAIXO RETORNA OS MENSALISTAS/ATUALIZA/CADASTRA/DELETA

def lista_mensalistas(request):
    mensalistas = Mensalista.objects.all()
    forms = MensalistaForm()
    data =  {'mensalistas': mensalistas, 'forms': forms}
    return render(request, 'core/lista_mensalistas.html', data)

def novo_mensalista(request):
    form = MensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_mensalistas')

def mensalista_update(request, id):
    data = {}
    mensalista = Mensalista.objects.get(id=id)
    form = MensalistaForm(request.POST or None, instance=mensalista) 
    data['mensalista'] = mensalista
    data['form'] = form

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('core_lista_mensalistas') 
    else:
        return render(request, 'core/mensalista_update.html', data)

def mensalista_delete(request, id):
    mensalista = Mensalista.objects.get(id=id)
    if request.method == 'POST':
        mensalista.delete()
        return redirect('core_lista_mensalistas')
    else:
        return render(request, 'core/mensalistaconfirme_delete.html', {'mensalista': mensalista})


# OS METODOS ABAIXO RETORNA OS MOVMENSALISTAS/ATUALIZA/CADASTRA/DELETA

def lista_movmensalistas(request):
    movmensalistas = MovMensalista.objects.all()
    forms = MovMensalistaForm()
    data = {'movmensalistas': movmensalistas, 'forms': forms}
    return render(
        request, 'core/lista_movmensalistas.html', data
    )

def novo_movmensalista(request):
    form = MovMensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_movmensalistas')


def movmensalista_update(request, id):
    data = {}
    movmensalista = MovMensalista.objects.get(id=id)
    form = MovMensalistaForm(request.POST or None, instance=movmensalista)
    data['movmensalista'] = movmensalista
    data['form'] = form

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('core_lista_movmensalistas')
    else:
        return render(request, 'core/movmensalista_update.html', data)

def movmensalista_delete(request, id):
    movmensalista = MovMensalista.objects.get(id=id)
    if request.method == 'POST':
        movmensalista.delete()
        return redirect('core_lista_mensalistas')
    else:
        return render(request, 'core/movmensalistaconfirme_delete.html', {'movmensalista': movmensalista})
