from django.shortcuts import render, redirect
from django import forms
from .models import Perfume, Resena, Perfumeria


class ResenaForm(forms.ModelForm):
    class Meta:
        model = Resena
        fields = ['nombre', 'comentario', 'puntuacion']


def inicio(request):
    top_perfumes = Perfume.objects.order_by('-ventas')[:4]
    top_perfumerias = Perfumeria.objects.all()[:5]
    resenas = Resena.objects.order_by('-fecha')[:6]
    return render(request, 'tienda/inicio.html', {
        'top_perfumes': top_perfumes,
        'top_perfumerias': top_perfumerias,
        'resenas': resenas,
    })


def catalogo(request):
    perfumes = Perfume.objects.all().order_by('nombre')
    return render(request, 'tienda/catalogo.html', {'perfumes': perfumes})


def resenas(request):
    lista = Resena.objects.order_by('-fecha')
    form = ResenaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('resenas')
    return render(request, 'tienda/resenas.html', {'resenas': lista, 'form': form})
