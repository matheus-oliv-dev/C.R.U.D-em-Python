import csv
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView, View
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Sum
from django.utils.timezone import now
from .models import Produto
from .forms import ProdutoForm

# View para Cadastro de Usuários (SignUp)
class CadastroUsuario(CreateView):
    """
    Controla o cadastro de novos usuários no sistema.
    Usa o formulário padrão do Django (UserCreationForm).
    """
    form_class = UserCreationForm
    success_url = reverse_lazy('login') # Redireciona para o login após criar a conta
    template_name = 'registration/signup.html'

# View para Listar Produtos (Read)
class ListarProdutos(LoginRequiredMixin, ListView):
    """
    Exibe a lista de todos os produtos cadastrados.
    Exige que o usuário esteja logado (LoginRequiredMixin).
    """
    model = Produto
    template_name = 'core/produto_list.html'
    ordering = ['nome_produto'] # Ordena a lista alfabeticamente
    login_url = 'login' # Se não estiver logado, manda para cá
    context_object_name = 'produtos' # Nome da variável para usar no template HTML
    paginate_by = 10 # Paginação: 10 itens por página

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(nome_produto__icontains=q)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('q', '')
        return context

# View para Criar Produto (Create)
class CriarProduto(LoginRequiredMixin, CreateView):
    """
    Exibe o formulário de cadastro e salva um novo produto.
    """
    model = Produto
    form_class = ProdutoForm # Usa nosso formulário com validação
    template_name = 'core/produto_form.html'
    success_url = reverse_lazy('produto_list') # Redireciona para a lista após salvar
    login_url = 'login'

# View para Editar Produto (Update)
class EditarProduto(LoginRequiredMixin, UpdateView):
    """
    Exibe o formulário preenchido e atualiza um produto existente.
    """
    model = Produto
    form_class = ProdutoForm
    template_name = 'core/produto_form.html' # Reutiliza o mesmo template de cadastro
    success_url = reverse_lazy('produto_list')
    login_url = 'login'

# View para Deletar Produto (Delete)
class DeletarProduto(LoginRequiredMixin, DeleteView):
    """
    Exibe a página de confirmação e exclui o produto.
    """
    model = Produto
    template_name = 'core/produto_confirm_delete.html'
    success_url = reverse_lazy('produto_list')
    login_url = 'login'
    context_object_name = 'produto' # Nome da variável para usar no template HTML

# View para o Dashboard
@method_decorator(cache_page(60 * 15), name='dispatch')
class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'core/dashboard.html'
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        hoje = now().date()
        
        # Total de produtos
        total_produtos = Produto.objects.count()
        
        # Produtos cadastrados hoje
        produtos_hoje = Produto.objects.filter(data_cadastro__date=hoje).count()
        
        # Valor total em estoque (soma de todos os valores)
        valor_estoque = Produto.objects.aggregate(Sum('valor'))['valor__sum'] or 0
        
        # Últimos 5 produtos
        ultimos_produtos = Produto.objects.order_by('-data_cadastro')[:5]

        context['total_produtos'] = total_produtos
        context['produtos_hoje'] = produtos_hoje
        context['valor_estoque'] = valor_estoque
        context['ultimos_produtos'] = ultimos_produtos
        return context

# View para Exportar Relatório em CSV
class ExportarProdutosCSV(LoginRequiredMixin, View):
    """
    Gera e faz o download de um relatório CSV de todos os produtos.
    """
    login_url = 'login'

    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="relatorio_produtos.csv"'

        writer = csv.writer(response)
        # Cabeçalho da tabela
        writer.writerow(['ID', 'Nome do Produto', 'Valor (R$)', 'Data de Cadastro'])

        # Busca produtos
        produtos = Produto.objects.all().order_by('-data_cadastro')
        for produto in produtos:
            writer.writerow([
                produto.id,
                produto.nome_produto,
                produto.valor,
                produto.data_cadastro.strftime('%d/%m/%Y %H:%M') if produto.data_cadastro else ''
            ])

        return response
