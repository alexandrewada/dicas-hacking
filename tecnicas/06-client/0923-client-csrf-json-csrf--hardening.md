---
id: "0923"
categoria: "06-client"
familia: "client-csrf"
slug: "json-csrf"
angulo: "hardening"
mitre: ""
owasp: ""
tags: ["06-client", "client-csrf", "hardening"]
aliases: ["JSON CSRF via text/plain", "json-csrf", "json-csrf-hardening"]
---

# JSON CSRF via text/plain — hardening

Do PoC ao controle — JSON CSRF via text/plain.

## Risco

CSRF força o browser autenticado a emitir requests state-changing.
Defesas (tokens, SameSite, Origin) falham por misconfig, method override, JSON com content-types
permissivos e XSS que lê tokens. SameSite=Lax não cobre tudo (chrome changes, subdomain XSS).

## Controles desta variante

- **Flash legado / nav quirks.** Sem isso o playbook da família mente.
- SameSite ajuda; não substitui token em API cookie-based. State change cross-site com sessão válida.

## Camadas

1) Bloqueio imediato
2) Origin failures; CSRF token mismatch metrics.
3) Anti-CSRF tokens; SameSite=Strict/Lax consciente; Preferir Authorization header;
re-auth para ações críticas.
Reteste com o mesmo PoC — critério: a prova desta variante falha.

## PoC mínimo

```text
checklist json-csrf:
- [ ] controle preventivo ativo
- [ ] telemetria cobre o PoC
- [ ] reteste com mesma prova (adc219) falha
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

- [JSON CSRF via text/plain](0163-client-csrf-json-csrf.md)
- [JSON CSRF via text/plain — lab](0543-client-csrf-json-csrf--lab.md)
- [clickjacking + CSRF](0170-client-csrf-clickjacking.md)
- [CORS reflection + CSRF](0169-client-csrf-cors.md)
- [logout CSRF](0168-client-csrf-logout.md)
- [X-HTTP-Method-Override](0164-client-csrf-method-override.md)