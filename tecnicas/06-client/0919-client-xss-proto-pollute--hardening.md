---
id: "0919"
categoria: "06-client"
familia: "client-xss"
slug: "proto-pollute"
angulo: "hardening"
mitre: "T1189"
owasp: "WSTG-INPV-01"
tags: ["06-client", "client-xss", "hardening", "t1189"]
aliases: ["prototype pollution → XSS", "proto-pollute", "proto-pollute-hardening"]
---

# prototype pollution → XSS — hardening

Do PoC ao controle — prototype pollution → XSS.

## Risco

XSS moderno raramente é `alert(1)`: o valor está em roubo de sessão, bypass de CSRF,
abuso de WebMessages e chain com CSP bypass. DOM XSS exige data flow (source→sink) real.

## Controles desta variante

- **jQuery sinks etc.** Sem isso o playbook da família mente.
- Sink + contexto + cookie flags. Encadeio até ação autenticada ou token se HttpOnly falhar.
- Gadget até sink. Sem gadget: hardening de merge, severidade menor.

## Camadas

Controle que fecha: HttpOnly+Secure+SameSite; CSP nonce/hash; sanitização server+client;
Trusted Types.
Sinal que deveria existir: CSP reports; WAF XSS signatures; canary cookies.

## No lab ficou assim

```text
checklist proto-pollute:
- [ ] controle preventivo ativo
- [ ] telemetria cobre o PoC
- [ ] reteste com mesma prova (e37a19) falha
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

- [prototype pollution → XSS](0159-client-xss-proto-pollute.md)
- [prototype pollution → XSS — lab](0539-client-xss-proto-pollute--lab.md)
- [template injection client (Angular/Vue)](0158-client-xss-angular.md)
- [XSS até account takeover](0160-client-xss-ato-chain.md)
- [CSP bypass gadgets](0155-client-xss-csp-bypass.md)
- [DOM XSS](0153-client-xss-dom.md)