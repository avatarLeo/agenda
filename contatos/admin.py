from django.contrib import admin
from .models import Contato, Categoria

class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'telefone', 'email', 'data_criacao', 'mostrar')
    list_display_links = ('nome', 'sobrenome')
    #list_filter = ('nome', 'sobrenome')
    list_per_page = 10
    search_fields = ('nome', 'sobrenome', 'telefone')
    list_editable = ('mostrar', 'telefone')
    list_filter = 'data_criacao',

admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)
