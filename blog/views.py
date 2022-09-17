
from django.shortcuts import render, redirect
from .models import Postagem
from .forms import FormularioPostagem

def home(request):
    postagens = Postagem.objects.all()
    data = {}
    data['postagens'] = postagens
    return render(request, 'blog/home.html', data) # ok

def create(request):    
    form = FormularioPostagem(request.POST or None)
    data = {}
    data['form'] = form

    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'blog/create.html', data) # ok   

def leitura_postagem(request, pk):
    postagem = Postagem.objects.get(pk=pk)
    data = {}
    data['postagem'] = postagem
    return render(request, 'blog/postagem.html', data) # ok

def update(request, pk):
    postagem = Postagem.objects.get(pk=pk)   
    form = FormularioPostagem(request.POST or None, instance=postagem) 
    data = {}
    data['postagem'] = postagem
    data['form'] = form  

    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'blog/update.html', data) # ok  

def delete(request, pk):
    postagem = Postagem.objects.get(pk=pk)  
    postagem.delete()

    return redirect('home') # ok