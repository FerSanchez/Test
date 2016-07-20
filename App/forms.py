from django import forms

from .models import Libros,Autores

class LibrosForm(forms.ModelForm):
    class Meta:
        model=Libros
        fields=[
            "Nombre",
            "Genero",
            "Descripcion",
            "Portada",

        ]

class AutoresForm(forms.ModelForm):
    class Meta:
        model=Autores
        fields=[
            "Nombre",
            "libros",
            "Nacionalidad",
            "Descripcion",

        ]
