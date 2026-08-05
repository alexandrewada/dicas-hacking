---
id: "0915"
categoria: "06-client"
familia: "client-xss"
slug: "csp-bypass"
angulo: "hardening"
mitre: ""
owasp: "WSTG-INPV-01"
tags: ["06-client", "client-xss", "hardening"]
aliases: ["CSP bypass gadgets", "csp-bypass", "csp-bypass-hardening"]
---

# CSP bypass gadgets — hardening

Do PoC ao controle — CSP bypass gadgets.

## Risco

XSS moderno raramente é `alert(1)`: o valor está em roubo de sessão, bypass de CSRF,
abuso de WebMessages e chain com CSP bypass. DOM XSS exige data flow (source→sink) real.

## Controles desta variante

- Se não validar **JSONP, CDNs antigos, nonce leak**, a nota fica genérica.
- Sink + contexto + cookie flags. Encadeio até ação autenticada ou token se HttpOnly falhar.

## Camadas

Hotfix: quebra a exploração direta de CSP bypass gadgets.
Detectivo: CSP reports; WAF XSS signatures; canary cookies.
Estrutural: HttpOnly+Secure+SameSite; CSP nonce/hash; sanitização server+client;
Trusted Types.

## Exemplo

```text
antes: controle ausente para csp-bypass
depois: ownership check / deny default em TARGET
verificação: PoC c9da58 retorna 403/blocked
reteste USER_A vs USER_B
```

## Armadilha

Não capture sessões de usuários reais. Evito defacement.

## Antes/depois

PoC HTML; cookie flags; impacto narrado.

Aceite de risco só por escrito, com prazo.

## Refs

- [WSTG-INPV-01](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/01-Testing_for_Reflected_Cross_Site_Scripting)
- [PortSwigger — XSS](https://portswigger.net/web-security/cross-site-scripting)
- [OWASP XSS Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)

## Relacionadas

- [CSP bypass gadgets](0155-client-xss-csp-bypass.md)
- [CSP bypass gadgets — lab](0535-client-xss-csp-bypass--lab.md)
- [template injection client (Angular/Vue)](0158-client-xss-angular.md)
- [XSS até account takeover](0160-client-xss-ato-chain.md)
- [DOM XSS](0153-client-xss-dom.md)
- [mutation XSS (mXSS)](0156-client-xss-mutation.md)