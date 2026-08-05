---
id: "0531"
categoria: "06-client"
familia: "client-xss"
slug: "reflected"
angulo: "lab"
mitre: ""
owasp: "WSTG-INPV-01"
tags: ["06-client", "client-xss", "lab"]
aliases: ["reflected XSS", "reflected", "reflected-lab"]
---

# reflected XSS — lab

Sandbox throwaway — reflected XSS sem ruído de cliente.

## Contexto

XSS moderno raramente é `alert(1)`: o valor está em roubo de sessão, bypass de CSRF,
abuso de WebMessages e chain com CSP bypass. DOM XSS exige data flow (source→sink) real.

## Variante

- Se não validar **Param → response sem encoding**, a nota fica genérica.
- Sink + contexto + cookie flags. Encadeio até ação autenticada ou token se HttpOnly falhar.

## Setup

Ativo mínimo. Duas identidades se for authz.
Restore point.

## Fluxo

1. Mapeio reflections e sinks DOM (innerHTML, location, postMessage).
2. Testo contextos (HTML, attr, JS, URL, CSS).
3. Avalio cookies HttpOnly e CSP.
4. Construir PoC de impacto (sessão de teste / ação).
5. Verifico mutação por sanitizers (DOMPurify misconfig).

## Exemplo

```html
<!-- reflected/stored lab payload — sem persistir em prod -->
<img src=x onerror="fetch('https://oast.lab.local/0276bb')">
<!-- sink reflected: sessão USER_A / cookie flags -->
```

## Pitfall

Não capture sessões de usuários reais. Evito defacement.

XSS/CSRF: preciso do sink e da condição de auth. alert(1) sem abuso de sessão é demo.

## Prova do lab

PoC HTML; cookie flags; impacto narrado.

## Refs

- [WSTG-INPV-01](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/01-Testing_for_Reflected_Cross_Site_Scripting)
- [PortSwigger — XSS](https://portswigger.net/web-security/cross-site-scripting)
- [OWASP XSS Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)

## Relacionadas

- [reflected XSS](0151-client-xss-reflected.md)
- [reflected XSS — hardening](0911-client-xss-reflected--hardening.md)
- [template injection client (Angular/Vue)](0158-client-xss-angular.md)
- [XSS até account takeover](0160-client-xss-ato-chain.md)
- [CSP bypass gadgets](0155-client-xss-csp-bypass.md)
- [DOM XSS](0153-client-xss-dom.md)