from django.contrib import admin
from .models import Produto

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    """
    Configuração da área administrativa para o modelo Produto.
    Define o que aparece na listagem e filtros do painel do Django Admin.
    """
    list_display = ('nome_produto', 'valor') # Colunas que aparecem na tabela
    search_fields = ('nome_produto',)        # Campo de busca
    list_filter = ('valor',)                 # Filtro lateral
    ordering = ('nome_produto',)             # Ordenação padrão
