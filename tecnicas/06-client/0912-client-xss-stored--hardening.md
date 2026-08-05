---
id: "0912"
categoria: "06-client"
familia: "client-xss"
slug: "stored"
angulo: "hardening"
mitre: "T1189"
owasp: "WSTG-INPV-01"
tags: ["06-client", "client-xss", "hardening", "t1189"]
aliases: ["stored XSS", "stored", "stored-hardening"]
---

# stored XSS — hardening

Do PoC ao controle — stored XSS.

## Risco

XSS moderno raramente é `alert(1)`: o valor está em roubo de sessão, bypass de CSRF,
abuso de WebMessages e chain com CSP bypass. DOM XSS exige data flow (source→sink) real.

## Controles desta variante

- Se não validar **Perfil, markdown, suporte**, a nota fica genérica.
- Sink + contexto + cookie flags. Encadeio até ação autenticada ou token se HttpOnly falhar.

## Camadas

Hotfix: quebra a exploração direta de stored XSS.
Detectivo: CSP reports; WAF XSS signatures; canary cookies.
Estrutural: HttpOnly+Secure+SameSite; CSP nonce/hash; sanitização server+client;
Trusted Types.

## PoC mínimo

```bash
# verificação pós-hardening stored
curl -sk -o /dev/null -w '%{http_code}\n' https://app.lab.local/stored/obj_ec9937 \
  -H 'Cookie: session=USER_B'
# esperado 403 — tag ec9937
```

## Armadilha

Não capture sessões de usuários reais. Evito defacement.

## Antes/depois

PoC HTML; cookie flags; impacto narrado.

Aceite de risco só por escrito, com prazo.

## Refs

- [MITRE ATT&CK T1189](https://attack.mitre.org/techniques/T1189/)
- [MITRE ATT&CK T1059.007](https://attack.mitre.org/techniques/T1059/007/)
- [WSTG-INPV-01](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/01-Testing_for_Reflected_Cross_Site_Scripting)
- [PortSwigger — XSS](https://portswigger.net/web-security/cross-site-scripting)
- [OWASP XSS Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)

## Relacionadas

- [stored XSS](0152-client-xss-stored.md)
- [stored XSS — lab](0532-client-xss-stored--lab.md)
- [template injection client (Angular/Vue)](0158-client-xss-angular.md)
- [XSS até account takeover](0160-client-xss-ato-chain.md)
- [CSP bypass gadgets](0155-client-xss-csp-bypass.md)
- [DOM XSS](0153-client-xss-dom.md)
- [ausência total de token (path)](0161-client-csrf-token-missing.md)
- [leak via Referer (path)](../04-auth/0115-auth-oauth-oidc-referrer.md)