# 📊 TechSales - Dashboard & CRUD System

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white"/>
  <img src="https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white"/>
  <img src="https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white"/>
  <img src="https://img.shields.io/badge/Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white"/>
</p>

Bem-vindo ao **TechSales**! Este projeto é uma evolução completa de um script simples de terminal (CLI) para uma **aplicação web robusta e visualmente impressionante**, desenvolvida em Django.

O foco deste projeto é demonstrar habilidades full-stack: desde a arquitetura de banco de dados e autenticação no backend, até a criação de uma interface de usuário premium baseada no estilo *Glassmorphism* com Dark Mode nativo.

🔗 **[Acesse o projeto online no Vercel](https://c-r-u-d-em-python.vercel.app/)**

---

## ✨ Funcionalidades (Features)

*   **Dashboard Analítico:** Visão geral com métricas calculadas em tempo real (Total de produtos, itens adicionados no dia e valor total em estoque).
*   **Gestão de Produtos (CRUD):** Criação, leitura, atualização e exclusão completa de produtos do estoque.
*   **Autenticação de Usuários:** Sistema completo de login, logout e cadastro de novos usuários integrado com a segurança nativa do Django.
*   **Interface Premium (Glassmorphism):** Design responsivo feito à mão com CSS moderno, apresentando painéis translúcidos, botões interativos e tipografia legível (Google Fonts).
*   **Deploy Otimizado para Portfólio:** Hospedado no Vercel utilizando um banco de dados efêmero. O banco se limpa periodicamente, garantindo que recrutadores possam testar as funcionalidades de alteração/exclusão (Interactive Demo) sem comprometer permanentemente a integridade do portfólio.

---

## 🛠️ Tecnologias Utilizadas

*   **Backend:** Python & Django (Class-Based Views, Models, Forms)
*   **Frontend:** HTML5, Vanilla CSS (Glassmorphism), Bootstrap 5 (Grids & Componentes), Bootstrap Icons
*   **Banco de Dados:** SQLite (Configurado dinamicamente para rodar na pasta `/tmp` em ambientes serverless)
*   **Hospedagem & Deploy:** Vercel (com `WhiteNoise` para servir os arquivos estáticos de forma eficiente)

---

## 🚀 Como Rodar Localmente

Se desejar testar o projeto na sua própria máquina, siga os passos abaixo:

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/MATHEUS111JUNDIAI/C.R.U.D-em-Python.git
   cd C.R.U.D-em-Python
   ```

2. **Crie e ative o ambiente virtual:**
   ```bash
   python -m venv venv
   # No Windows:
   venv\Scripts\activate
   # No Linux/Mac:
   source venv/bin/activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute as migrações do banco de dados:**
   ```bash
   python manage.py migrate
   ```

5. **(Opcional) Crie um superusuário para acessar o painel Admin:**
   ```bash
   python manage.py createsuperuser
   ```

6. **Inicie o servidor de desenvolvimento:**
   ```bash
   python manage.py runserver
   ```

Acesse `http://127.0.0.1:8000` no seu navegador!

---
*Desenvolvido como projeto de portfólio para demonstrar proficiência em desenvolvimento Web com Python/Django.*
