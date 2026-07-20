# Arquitetura e Deploy (Vercel)

## Ambiente Serverless
O projeto é hospedado no Vercel, o que impõe a regra de sistema de arquivos Read-Only (Apenas Leitura).
A única pasta onde temos permissão de escrita e leitura durante a execução é a `/tmp/`.

## Gerenciamento de Estáticos
O `WhiteNoise` está configurado para servir arquivos estáticos em produção de forma eficiente via backend sem necessidade de CDN de terceiros.

## Segurança e Cache
- **Rate Limit:** Implementamos o `RateLimitMiddleware` nativamente para evitar spams e testes de carga nas rotas POST, limitando a 10 requisições por IP por minuto.
- **Cache:** O cache do Django usa o `FileBasedCache` gravando em `/tmp/django_cache`. O Dashboard utiliza `@cache_page(60 * 15)` para cachear resultados caros matemáticos do banco de dados (sum e count).
- **Sessões:** O aplicativo utiliza Signed Cookies (`SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'`) para manter o usuário logado, independentemente de qual nó ou servidor efêmero (serverless) do Vercel for ativado para responder o request.
