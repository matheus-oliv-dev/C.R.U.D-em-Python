from django.urls import path
from .views import ListarProdutos, CriarProduto, EditarProduto, DeletarProduto, CadastroUsuario, DashboardView, ExportarProdutosCSV

urlpatterns = [
    # Dashboard (Página Inicial)
    path('', DashboardView.as_view(), name='dashboard'),
    
    # Rota de Produtos e Relatórios
    path('produtos/', ListarProdutos.as_view(), name='produto_list'),
    path('exportar/', ExportarProdutosCSV.as_view(), name='produto_export_csv'),
    
    # Rotas de CRUD
    path('novo/', CriarProduto.as_view(), name='produto_create'),
    path('editar/<int:pk>/', EditarProduto.as_view(), name='produto_update'),
    path('deletar/<int:pk>/', DeletarProduto.as_view(), name='produto_delete'),
    
    # Rota de Cadastro de Usuário
    path('signup/', CadastroUsuario.as_view(), name='signup'),
]
