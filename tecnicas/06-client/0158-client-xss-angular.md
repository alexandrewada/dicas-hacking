# template injection client (Angular/Vue)

## Contexto

XSS moderno raramente é `alert(1)`: o valor está em roubo de sessão, bypass de CSRF,
abuso de WebMessages e chain com CSP bypass. DOM XSS exige data flow (source→sink) real.

## Detalhe

- Detalhe que pago pra ver: **SSTI client-side**.
- Sink + contexto + cookie flags. Encadeio até ação autenticada ou token se HttpOnly falhar.

## Execução

1. Mapeio reflections e sinks DOM (innerHTML, location, postMessage).
2. Testo contextos (HTML, attr, JS, URL, CSS).
3. Avalio cookies HttpOnly e CSP.
4. Construir PoC de impacto (sessão de teste / ação).
5. Verifico mutação por sanitizers (DOMPurify misconfig).

## PoC mínimo

```html
<!-- reflected/stored lab payload — sem persistir em prod -->
<img src=x onerror="fetch('https://oast.lab.local/701689')">
<!-- sink angular: sessão USER_A / cookie flags -->
```

## OpSec

Não persisto payload em produção sem janela e plano de purge.

## Cuidados

Não capture sessões de usuários reais. Evito defacement.

## Fechamento

| | |
|---|---|
| Detecção | CSP reports; WAF XSS signatures; canary cookies. |
| Remediação | HttpOnly+Secure+SameSite; CSP nonce/hash; sanitização server+client;
Trusted Types. |
| Evidência | PoC HTML; cookie flags; impacto narrado. |

## Refs

- PortSwigger XSS
- OWASP XSS
- WSTG-INPV-01/02