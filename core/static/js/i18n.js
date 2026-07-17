document.addEventListener("DOMContentLoaded", () => {
    // 1. Verificar o idioma atual salvo (ou padrão 'pt')
    let currentLang = localStorage.getItem('app_lang') || 'pt';
    
    const langBtn = document.getElementById('lang-toggle');
    const elementsToTranslate = document.querySelectorAll('[data-i18n]');
    
    // 2. Função principal de tradução
    function applyTranslations(lang) {
        elementsToTranslate.forEach(el => {
            const key = el.getAttribute('data-i18n');
            if (window.translations[lang] && window.translations[lang][key]) {
                // Se o elemento contiver tags HTML dentro dele (como ícones),
                // precisamos tentar substituir apenas o texto final e manter o ícone.
                // Uma forma simples é envolvermos os textos traduzíveis em <span>, 
                // mas caso substituamos diretamente:
                
                // Vamos checar se o elemento já usa <span> internamente para o texto:
                const spanTarget = el.querySelector('.i18n-text');
                if (spanTarget) {
                    spanTarget.textContent = window.translations[lang][key];
                } else {
                    el.textContent = window.translations[lang][key];
                }
            }
        });
        
        // Atualizar visual do botão
        if(langBtn) {
            if (lang === 'pt') {
                langBtn.innerHTML = "🇺🇸 EN";
                langBtn.title = "Switch to English";
            } else {
                langBtn.innerHTML = "🇧🇷 PT";
                langBtn.title = "Mudar para Português";
            }
        }
    }
    
    // 3. Aplicar tradução inicial
    applyTranslations(currentLang);
    
    // 4. Lidar com o clique do botão
    if(langBtn) {
        langBtn.addEventListener('click', (e) => {
            e.preventDefault();
            // Alterna o idioma
            currentLang = currentLang === 'pt' ? 'en' : 'pt';
            localStorage.setItem('app_lang', currentLang);
            applyTranslations(currentLang);
        });
    }
});
