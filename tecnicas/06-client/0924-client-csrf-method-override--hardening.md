---
id: "0924"
categoria: "06-client"
familia: "client-csrf"
slug: "method-override"
angulo: "hardening"
mitre: ""
owasp: ""
tags: ["06-client", "client-csrf", "hardening"]
aliases: ["X-HTTP-Method-Override", "method-override", "method-override-hardening"]
---

# X-HTTP-Method-Override — hardening

Do PoC ao controle — X-HTTP-Method-Override.

## Risco

CSRF força o browser autenticado a emitir requests state-changing.
Defesas (tokens, SameSite, Origin) falham por misconfig, method override, JSON com content-types
permissivos e XSS que lê tokens. SameSite=Lax não cobre tudo (chrome changes, subdomain XSS).

## Controles desta variante

- **Bypass de checks GET** — muda ruído e o que entra no PDF.
- SameSite ajuda; não substitui token em API cookie-based. State change cross-site com sessão válida.

## Camadas

Controle que fecha: Anti-CSRF tokens; SameSite=Strict/Lax consciente; Preferir Authorization header;
re-auth para ações críticas.
Sinal que deveria existir: Origin failures; CSRF token mismatch metrics.

## PoC mínimo

```bash
# verificação pós-hardening method-override
curl -sk -o /dev/null -w '%{http_code}\n' https://app.lab.local/method-override/a1b2c3d4-e5f6-7890-abcd-ef1234567890 \
  -H 'Cookie: session=USER_B'
# esperado 403 — tag 4e1504
```

## Armadilha

Login CSRF também importa. Não executo ações em contas alheias.

## Antes/depois

PoC HTML; request forjado; efeito na conta teste.

Aceite de risco só por escrito, com prazo.

## Refs

- [OWASP CSRF Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)
- [PortSwigger — CSRF](https://portswigger.net/web-security/csrf)

## Relacionadas

- [X-HTTP-Method-Override](0164-client-csrf-method-override.md)
- [X-HTTP-Method-Override — lab](0544-client-csrf-method-override--lab.md)
- [clickjacking + CSRF](0170-client-csrf-clickjacking.md)
- [CORS reflection + CSRF](0169-client-csrf-cors.md)
- [JSON CSRF via text/plain](0163-client-csrf-json-csrf.md)
- [logout CSRF](0168-client-csrf-logout.md)