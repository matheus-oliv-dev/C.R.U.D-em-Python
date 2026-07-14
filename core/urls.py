from django.urls import path
from .views import ListarProdutos, CriarProduto, EditarProduto, DeletarProduto, CadastroUsuario, DashboardView

urlpatterns = [
    # Dashboard (Página Inicial)
    path('', DashboardView.as_view(), name='dashboard'),
    
    # Rota de Produtos
    path('produtos/', ListarProdutos.as_view(), name='produto_list'),
    
    # Rotas de CRUD
    path('novo/', CriarProduto.as_view(), name='produto_create'),
    path('editar/<int:pk>/', EditarProduto.as_view(), name='produto_update'),
    path('deletar/<int:pk>/', DeletarProduto.as_view(), name='produto_delete'),
    
    # Rota de Cadastro de Usuário
    path('signup/', CadastroUsuario.as_view(), name='signup'),
]
