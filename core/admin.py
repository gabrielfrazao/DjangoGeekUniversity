from django.contrib import admin

# Register your models here.

from .models import Produto, Pacientes

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque')

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'idade', 'sexo', 'email')


admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Pacientes)

