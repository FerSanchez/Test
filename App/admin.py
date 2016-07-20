from django.contrib import admin
from .models import Libros
from .models import Autores

admin.site.register(Libros)
admin.site.register(Autores)
