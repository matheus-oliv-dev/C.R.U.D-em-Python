# Regras de Banco de Dados

## ORM do Django
Sempre utilize o ORM nativo do Django (`Model.objects...`). É terminantemente proibido o uso de consultas SQL puras (`.raw()`) sem extrema necessidade de performance, para blindar a API contra injeções de SQL.

## Localização do SQLite
Em produção (Vercel), o SQLite é forçado a rodar em `/tmp/db.sqlite3`.
Para deploys, a versão mais recente do `db.sqlite3` na raiz do repositório será clonada para o `/tmp/` no momento do cold-start, como configurado via bootstrap em `projeto_crud/settings.py`.

## Migrações (Migrations)
Nunca apague a pasta `migrations/` dos apps. Sempre comite os arquivos gerados pelo comando `makemigrations` para garantir estabilidade no ambiente de produção.
