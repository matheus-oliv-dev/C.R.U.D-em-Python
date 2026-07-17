const translations = {
    pt: {
        // base.html
        "nav_dashboard": "Dashboard",
        "nav_produtos": "Produtos",
        "nav_portfolio": "Portfólio",
        "nav_ola": "Olá",
        "nav_sair": "Sair",
        "nav_entrar": "Entrar",
        "nav_cadastrar": "Cadastrar",
        
        // dashboard.html
        "dash_title": "Visão Geral do Estoque",
        "dash_subtitle": "Acompanhe as principais métricas dos seus produtos.",
        "dash_total": "Total de Produtos",
        "dash_hoje": "Adicionados Hoje",
        "dash_valor": "Valor em Estoque",
        "dash_ultimos": "Últimos Produtos Cadastrados",
        "dash_ver_todos": "Ver todos",
        "table_nome": "Nome",
        "table_data": "Data de Cadastro",
        "table_valor": "Valor",
        "table_empty_dash": "Nenhum produto recente.",

        // produto_list.html
        "list_title": "Produtos em Estoque",
        "list_novo": "Novo Produto",
        "list_exportar": "Exportar CSV",
        "list_editar": "Editar",
        "list_excluir": "Excluir",
        "list_empty": "Nenhum produto cadastrado.",

        // forms & delete
        "form_title_create": "Cadastrar Produto",
        "form_title_edit": "Editar Produto",
        "form_save": "Salvar",
        "form_cancel": "Cancelar",
        "label_nome_produto": "Nome do Produto",
        "label_valor": "Preço (R$)",
        "delete_title": "Confirmar Exclusão",
        "delete_msg": "Tem certeza que deseja excluir o produto",
        "delete_warning": "Esta ação é permanente e não poderá ser desfeita.",
        "delete_btn": "Sim, Excluir",

        // Auth
        "auth_login_title": "Acesso Restrito",
        "auth_signup_title": "Novo Cadastro",
        "auth_error": "Usuário ou senha incorretos. Tente novamente.",
        "auth_already": "Já tem conta? Entre aqui.",
        "label_username": "Usuário",
        "label_password": "Senha",
        "label_password1": "Senha",
        "label_password2": "Confirmação de Senha"
    },
    en: {
        // base.html
        "nav_dashboard": "Dashboard",
        "nav_produtos": "Products",
        "nav_portfolio": "Portfolio",
        "nav_ola": "Hello",
        "nav_sair": "Logout",
        "nav_entrar": "Login",
        "nav_cadastrar": "Sign Up",
        
        // dashboard.html
        "dash_title": "Inventory Overview",
        "dash_subtitle": "Track your products' main metrics.",
        "dash_total": "Total Products",
        "dash_hoje": "Added Today",
        "dash_valor": "Total Value",
        "dash_ultimos": "Recent Products",
        "dash_ver_todos": "View All",
        "table_nome": "Name",
        "table_data": "Registration Date",
        "table_valor": "Value",
        "table_empty_dash": "No recent products.",

        // produto_list.html
        "list_title": "Products in Stock",
        "list_novo": "New Product",
        "list_exportar": "Export CSV",
        "list_editar": "Edit",
        "list_excluir": "Delete",
        "list_empty": "No products registered.",

        // forms & delete
        "form_title_create": "Register Product",
        "form_title_edit": "Edit Product",
        "form_save": "Save",
        "form_cancel": "Cancel",
        "label_nome_produto": "Product Name",
        "label_valor": "Price ($)",
        "delete_title": "Confirm Deletion",
        "delete_msg": "Are you sure you want to delete the product",
        "delete_warning": "This action is permanent and cannot be undone.",
        "delete_btn": "Yes, Delete",

        // Auth
        "auth_login_title": "Restricted Access",
        "auth_signup_title": "New Registration",
        "auth_error": "Invalid username or password. Please try again.",
        "auth_already": "Already have an account? Login here.",
        "label_username": "Username",
        "label_password": "Password",
        "label_password1": "Password",
        "label_password2": "Password Confirmation"
    }
};

// Exportar para uso no i18n.js (se usando modules) ou deixar globalmente acessível
window.translations = translations;
