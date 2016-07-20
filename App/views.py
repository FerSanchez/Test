from django.shortcuts import render
from django.template import loader
from models import Libros, Autores
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .forms import LibrosForm,AutoresForm


def index(request):
    all_books= Libros.objects.all()
    return render(request,'App/index.html', {'all_books': all_books})

def indexA(request):
    all_autores= Autores.objects.all()
    return render(request,'App/autorindex.html' , {'all_autores': all_autores})

def detalle(request, libro_id):
    libro= get_object_or_404(Libros, pk=libro_id)
    return render(request, 'App/detalle.html',{'libro': libro} )

def detailA(request, autor_id):
    autor= get_object_or_404(Autores, pk=autor_id)
    return render(request, 'App/detailA.html',{'autor': autor} )

def borrarA(request, autor_id):
    query=get_object_or_404(Autores, pk=autor_id)
    query.delete()
    return HttpResponseRedirect('/libros/indexA/')

def actualizarA(request, autor_id):
    query=get_object_or_404(Autores, pk=autor_id)
    form = AutoresForm(request.POST or None, request.FILES or None, instance = query)
    if form.is_valid():
        post = form.save(commit = False)
        post.save()
        return HttpResponseRedirect('/libros/indexA')
    context = {
        "detalle":query,
        "form":form,
    }
    return render(request,'App/editarA.html',context)

def crearA(request):
    form = AutoresForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        post = form.save(commit = False)
        post.save()
        return HttpResponseRedirect('/libros/indexA')
    context = {
        "form":form,
    }
    return render(request,'App/editarA.html',context)



def borrar(request, libro_id):
    query=get_object_or_404(Libros, pk=libro_id)
    query.delete()
    return HttpResponseRedirect('/libros/')

def actualizar(request, libro_id):
    query=get_object_or_404(Libros, pk=libro_id)
    form = LibrosForm(request.POST or None, request.FILES or None, instance = query)
    if form.is_valid():
        post = form.save(commit = False)
        post.save()
        return HttpResponseRedirect('/libros/')
    context = {
        "detalle":query,
        "form":form,
    }
    return render(request,'App/editar.html',context)

def crear(request):
    form = LibrosForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        post = form.save(commit = False)
        post.save()
        return HttpResponseRedirect('/libros/')
    context = {
        "form":form,
    }
    return render(request,'App/editar.html',context)
