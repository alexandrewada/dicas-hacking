# mutation XSS (mXSS)

**A03 Injection** · `T1189 Drive-by / T1059.007 JS`

## Contexto

XSS moderno raramente é `alert(1)`: o valor está em roubo de sessão, bypass de CSRF,
abuso de WebMessages e chain com CSP bypass. DOM XSS exige data flow (source→sink) real.

## O que muda aqui

- **Sanitizer breakage.** Sem isso o playbook da família mente.
- Sink + contexto + cookie flags. Encadeio até ação autenticada ou token se HttpOnly falhar.

## Como testo

1. Mapeio reflections e sinks DOM (innerHTML, location, postMessage).
2. Testo contextos (HTML, attr, JS, URL, CSS).
3. Avalio cookies HttpOnly e CSP.
4. Construir PoC de impacto (sessão de teste / ação).
5. Verifico mutação por sanitizers (DOMPurify misconfig).

## Exemplo

```html
<!-- reflected/stored lab payload — sem persistir em prod -->
<img src=x onerror="fetch('https://oast.lab.local/db92c1')">
<!-- sink mutation: sessão USER_A / cookie flags -->
```

## Campo

Não persisto payload em produção sem janela e plano de purge.

Já abri High demais em mutation XSS (mXSS) por sintoma sem efeito. Cruzei com: CSP reports; WAF XSS signatures; canary cookies. Sem side-effect, baixo.

## Já me queimei

Não capture sessões de usuários reais. Evito defacement.

## Blue

- Detectar: CSP reports; WAF XSS signatures; canary cookies.
- Fechar: HttpOnly+Secure+SameSite; CSP nonce/hash; sanitização server+client;
Trusted Types.

## Evidência

PoC HTML; cookie flags; impacto narrado.

## Refs

- PortSwigger XSS
- OWASP XSS
- WSTG-INPV-01/02