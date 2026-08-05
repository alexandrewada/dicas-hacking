---
id: "0918"
categoria: "06-client"
familia: "client-xss"
slug: "angular"
angulo: "hardening"
mitre: ""
owasp: "WSTG-INPV-01"
tags: ["06-client", "client-xss", "hardening"]
aliases: ["template injection client (Angular/Vue)", "angular", "angular-hardening"]
---

# template injection client (Angular/Vue) — hardening

Do PoC ao controle — template injection client (Angular/Vue).

## Risco

XSS moderno raramente é `alert(1)`: o valor está em roubo de sessão, bypass de CSRF,
abuso de WebMessages e chain com CSP bypass. DOM XSS exige data flow (source→sink) real.

## Controles desta variante

- Detalhe que pago pra ver: **SSTI client-side**.
- Sink + contexto + cookie flags. Encadeio até ação autenticada ou token se HttpOnly falhar.

## Camadas

1) Bloqueio imediato
2) CSP reports; WAF XSS signatures; canary cookies.
3) HttpOnly+Secure+SameSite; CSP nonce/hash; sanitização server+client;
Trusted Types.
Reteste com o mesmo PoC — critério: a prova desta variante falha.

## No lab ficou assim

```bash
# verificação pós-hardening angular
curl -sk -o /dev/null -w '%{http_code}\n' https://app.lab.local/angular/a1b2c3d4-e5f6-7890-abcd-ef1234567890 \
  -H 'Cookie: session=USER_B'
# esperado 403 — tag 261231
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

- [template injection client (Angular/Vue)](0158-client-xss-angular.md)
- [template injection client (Angular/Vue) — lab](0538-client-xss-angular--lab.md)
- [XSS até account takeover](0160-client-xss-ato-chain.md)
- [CSP bypass gadgets](0155-client-xss-csp-bypass.md)
- [DOM XSS](0153-client-xss-dom.md)
- [mutation XSS (mXSS)](0156-client-xss-mutation.md)