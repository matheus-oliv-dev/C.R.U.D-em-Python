import time
from django.core.cache import cache
from django.http import HttpResponse

class RateLimitMiddleware:
    """
    Middleware customizado para bloquear ataques de spam ou robôs.
    Limita as requisições POST por IP utilizando o Cache nativo do Django.
    """
    def __init__(self, get_response):
        self.get_response = get_response
        self.limit = 10  # Máximo de requisições POST permitidas
        self.timeout = 60  # Janela de tempo de 60 segundos (1 minuto)

    def get_client_ip(self, request):
        """
        Garante a leitura do IP correto mesmo se hospedado atrás de um Proxy 
        como na Vercel (onde todo tráfego vem mascarado).
        """
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def __call__(self, request):
        # Aplicamos a proteção de metralhadora apenas para requisições de modificação
        if request.method == 'POST':
            ip = self.get_client_ip(request)
            cache_key = f"ratelimit_post_{ip}"
            
            # Recupera o histórico de requisições deste IP no último minuto
            history = cache.get(cache_key, [])
            current_time = time.time()
            
            # Limpa requisições antigas (fora da janela de 60s)
            history = [req_time for req_time in history if current_time - req_time < self.timeout]
            
            # Se já fez 10 requisições, devolve erro oficial 429
            if len(history) >= self.limit:
                html_response = """
                <!DOCTYPE html>
                <html>
                <head><title>429 Too Many Requests</title></head>
                <body style="font-family: Arial, sans-serif; background-color: #121212; color: #fff; text-align: center; padding-top: 100px;">
                    <h1 style="color: #f64a4a;">Proteção Anti-Spam Ativada</h1>
                    <h3 style="color: #a8a8a8;">Status 429 - Too Many Requests</h3>
                    <p>O limite de ações (10 por minuto) foi atingido.</p>
                    <p>Por favor, aguarde alguns segundos e tente novamente.</p>
                    <a href="/" style="color: #4da3ff; text-decoration: none; margin-top: 20px; display: inline-block;">Voltar para o site</a>
                </body>
                </html>
                """
                return HttpResponse(html_response, status=429)
            
            # Adiciona a requisição atual no histórico
            history.append(current_time)
            cache.set(cache_key, history, self.timeout)

        # Se passou na verificação, segue com o fluxo normal do Django
        response = self.get_response(request)
        return response
