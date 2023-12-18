from django.shortcuts import render, redirect
from . import models

def index(request):
    produtos = models.Produto.objects.all()
    return render(request, 'estoque/index.html', {'produtos': produtos})


def cadastrar_produto(request):
    if request.method == 'POST':
        fields = [
            'nome', 'codigo_produto', 'descricao', 'preco',
        ]
        
        field_values = {}
        for field in fields:
            value = request.POST.get(field)
            if value:
                if field == 'preco':
                    value = value.replace(',', '.')
                field_values[field] = value


        new_produto = models.Produto(**field_values)
        new_produto.save()
    return render(request, 'estoque/cadastrar-produto.html',)


def update_produto(request):
    id_produto = None
    if request.method == 'POST':
        fields = [
            'pk', 'nome', 'codigo_produto', 'descricao', 'preco',
        ]
        
        field_values = {}
        for field in fields:
            value = request.POST.get(field)
            if value:
                if field == 'preco':
                    value = value.replace(',', '.')
                if field == 'pk':
                    id_produto = value
                field_values[field] = value


        new_produto, created = models.Produto.objects.update_or_create(
        id=field_values['pk'],
        defaults=field_values
        )

    if request.method == 'GET':
        id_produto = request.GET.get('pk')
        
    produto = models.Produto.objects.get(pk=id_produto)
    
    return render(request, 'estoque/update-produto.html',{'produto': produto})


def delete_produto(request):
    if request.method == 'POST':
        value = request.POST.get('pk')
        if value:
            models.Produto.objects.filter(pk=value).delete()
    return redirect('estoque:index')