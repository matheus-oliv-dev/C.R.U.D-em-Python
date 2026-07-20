@echo off
echo [INFO] Iniciando validacao do codigo (Harness Feedback)...
echo [1] Checando sintaxe e estrutura do Django...
python manage.py check
if %errorlevel% neq 0 (
    echo [ERRO] Ocorreu um problema no manage.py check. O baseline esta quebrado! Conserte o erro antes de comecar.
    exit /b %errorlevel%
)
echo [OK] Tudo pronto! O projeto esta saudavel e pronto para a proxima feature.
