---
id: "0911"
categoria: "06-client"
familia: "client-xss"
slug: "reflected"
angulo: "hardening"
mitre: ""
owasp: "WSTG-INPV-01"
tags: ["06-client", "client-xss", "hardening"]
aliases: ["reflected XSS", "reflected", "reflected-hardening"]
---

# reflected XSS — hardening

Do PoC ao controle — reflected XSS.

## Risco

XSS moderno raramente é `alert(1)`: o valor está em roubo de sessão, bypass de CSRF,
abuso de WebMessages e chain com CSP bypass. DOM XSS exige data flow (source→sink) real.

## Controles desta variante

- Se não validar **Param → response sem encoding**, a nota fica genérica.
- Sink + contexto + cookie flags. Encadeio até ação autenticada ou token se HttpOnly falhar.

## Camadas

Controle que fecha: HttpOnly+Secure+SameSite; CSP nonce/hash; sanitização server+client;
Trusted Types.
Sinal que deveria existir: CSP reports; WAF XSS signatures; canary cookies.

## PoC mínimo

```bash
# verificação pós-hardening reflected
curl -sk -o /dev/null -w '%{http_code}\n' https://app.lab.local/reflected/a1b2c3d4-e5f6-7890-abcd-ef1234567890 \
  -H 'Cookie: session=USER_B'
# esperado 403 — tag b23312
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

- [reflected XSS](0151-client-xss-reflected.md)
- [reflected XSS — lab](0531-client-xss-reflected--lab.md)
- [template injection client (Angular/Vue)](0158-client-xss-angular.md)
- [XSS até account takeover](0160-client-xss-ato-chain.md)
- [CSP bypass gadgets](0155-client-xss-csp-bypass.md)
- [DOM XSS](0153-client-xss-dom.md)