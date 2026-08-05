---
id: "0152"
categoria: "06-client"
familia: "client-xss"
slug: "stored"
angulo: "base"
mitre: "T1189"
owasp: "WSTG-INPV-01"
tags: ["06-client", "client-xss", "base", "t1189"]
aliases: ["stored XSS", "stored"]
---

# stored XSS

**A03 Injection** · `T1189 Drive-by / T1059.007 JS`

## Contexto

XSS moderno raramente é `alert(1)`: o valor está em roubo de sessão, bypass de CSRF,
abuso de WebMessages e chain com CSP bypass. DOM XSS exige data flow (source→sink) real.

## O que muda aqui

- Se não validar **Perfil, markdown, suporte**, a nota fica genérica.
- Sink + contexto + cookie flags. Encadeio até ação autenticada ou token se HttpOnly falhar.

## Como testo

1. Mapeio reflections e sinks DOM (innerHTML, location, postMessage).
2. Testo contextos (HTML, attr, JS, URL, CSS).
3. Avalio cookies HttpOnly e CSP.
4. Construir PoC de impacto (sessão de teste / ação).
5. Verifico mutação por sanitizers (DOMPurify misconfig).

## No lab ficou assim

```html
<!-- reflected/stored lab payload — sem persistir em prod -->
<img src=x onerror="fetch('https://oast.lab.local/fb67eb')">
<!-- sink stored: sessão USER_A / cookie flags -->
```

## Campo

CSP bypass só se atravesso a política atual do alvo, não CSP de lab antiga.

Falso amigo em stored XSS: UI/log gritam, impacto não. Exijo CSP reports.

## Já me queimei

Não capture sessões de usuários reais. Evito defacement.

## Blue

- Detectar: CSP reports; WAF XSS signatures; canary cookies.
- Fechar: HttpOnly+Secure+SameSite; CSP nonce/hash; sanitização server+client;
Trusted Types.

## Evidência

PoC HTML; cookie flags; impacto narrado.

## Refs

- [MITRE ATT&CK T1189](https://attack.mitre.org/techniques/T1189/)
- [MITRE ATT&CK T1059.007](https://attack.mitre.org/techniques/T1059/007/)
- [WSTG-INPV-01](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/01-Testing_for_Reflected_Cross_Site_Scripting)
- [PortSwigger — XSS](https://portswigger.net/web-security/cross-site-scripting)
- [OWASP XSS Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)

## Relacionadas

- [stored XSS — lab](0532-client-xss-stored--lab.md)
- [stored XSS — hardening](0912-client-xss-stored--hardening.md)
- [template injection client (Angular/Vue)](0158-client-xss-angular.md)
- [XSS até account takeover](0160-client-xss-ato-chain.md)
- [CSP bypass gadgets](0155-client-xss-csp-bypass.md)
- [DOM XSS](0153-client-xss-dom.md)
- [ausência total de token (path)](0161-client-csrf-token-missing.md)
- [leak via Referer (path)](../04-auth/0115-auth-oauth-oidc-referrer.md)