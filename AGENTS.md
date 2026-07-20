# AGENTS.md

## Visão Geral do Projeto
Sistema de Vendas CRUD desenvolvido em Python/Django, hospedado no Vercel (Serverless).
O Frontend utiliza Vanilla CSS (estilo Glassmorphism), Bootstrap 5 e JS Puro.

## Antes de Escrever Código
1. Leia `progress.md` e `feature_list.json` para saber o estado atual.
2. Execute `./init.sh` (ou `init.bat` no Windows) para garantir que o projeto base compila e não contém erros.
3. Se o baseline estiver quebrado, conserte antes de criar novas features.

## Restrições Obrigatórias
- **Banco de Dados:** O banco é SQLite. Devido ao Vercel Serverless, ele é copiado para `/tmp/` no momento da inicialização. NUNCA adicione bibliotecas que assumam persistência de banco de dados no File System local, a menos que seja na pasta temporária.
- **Sessões e Rate Limit:** As sessões utilizam Signed Cookies (`SESSION_ENGINE`). O Cache do Rate Limit está configurado para `/tmp/django_cache`.
- **Views:** Sempre utilizar Django Class-Based Views (CBVs) no `views.py`.
- **Estilo de Frontend:** Mantenha a identidade visual translúcida (Glassmorphism). Não introduza frameworks CSS pesados adicionais sem necessidade.
- **Internacionalização:** A i18n é resolvida no cliente via JavaScript puro (`core/static/js/i18n.js`). Não use a lib de i18n nativa do Django para não perder performance.

## Documentos Temáticos
- Infraestrutura e Vercel (`docs/architecture.md`)
- Banco de Dados e ORM (`docs/database-rules.md`)

## Definição de Concluído (DoD)
Uma feature só está pronta quando:
- O comportamento alvo foi implementado perfeitamente.
- `./init.sh` passa (sem erros do `manage.py check`).
- `feature_list.json` foi atualizado.
- `progress.md` contém o status final do que foi feito.

## Fim de Sessão
1. Atualize `feature_list.json` (status + evidência).
2. Atualize `progress.md` com bloqueios e próximos passos.
3. O próximo agente deve ser capaz de ler esses logs e continuar o projeto imeditamente sem pedir explicações.
