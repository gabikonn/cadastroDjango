from django.shortcuts import render, redirect
from .models import novoCadastro
from .form import CadastroForm

def home(request):
    return render(request, 'cadastroapp/home.html')

def listagem(request):
    data = {}
    data['cadastros'] = novoCadastro.objects.all()
    return render(request, 'cadastroapp/home.html', data)

def novo_cadastro(request):
    data = {}
    form = CadastroForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_listagem')

    data['form'] = form
    return render(request, 'cadastroapp/form.html', data)

def update(request, pk):
    data = {}
    cadastro = novoCadastro.objects.get(pk=pk)
    form = CadastroForm(request.POST or None, instance=cadastro)
    
    if form.is_valid():
        form.save()
        return redirect('url_listagem')

    data['form'] = form
    return render(request, 'cadastroapp/form.html', data)

def delete(request, pk):
    cadastro = novoCadastro.objects.get(pk=pk)
    cadastro.delete()
    return redirect('url_listagem')
