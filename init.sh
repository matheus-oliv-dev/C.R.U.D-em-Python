#!/bin/bash
# Script de validação da saúde do repositório (Harness Feedback)
echo "🔍 Iniciando validação do código..."

echo "1. Checando sintaxe e estrutura do Django..."
python manage.py check
if [ $? -ne 0 ]; then
  echo "❌ Erro encontrado no manage.py check. O baseline está quebrado! Conserte o erro antes de começar."
  exit 1
fi

echo "✅ Tudo pronto! O projeto está saudável e pronto para a próxima feature."
