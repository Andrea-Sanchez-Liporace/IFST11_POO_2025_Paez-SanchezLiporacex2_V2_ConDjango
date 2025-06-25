# importo la librería admin de Django y los modelos que quiero registrar en el panel de administración.
from django.contrib import admin
from sistema.models import Perro, UsuarioAdoptante

# Registro los modelos para que aparezcan en el panel de administración
admin.site.register(Perro)
admin.site.register(UsuarioAdoptante)