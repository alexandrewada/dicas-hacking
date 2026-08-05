---
id: "0544"
categoria: "06-client"
familia: "client-csrf"
slug: "method-override"
angulo: "lab"
mitre: ""
owasp: ""
tags: ["06-client", "client-csrf", "lab"]
aliases: ["X-HTTP-Method-Override", "method-override", "method-override-lab"]
---

# X-HTTP-Method-Override — lab

Sandbox throwaway — X-HTTP-Method-Override sem ruído de cliente.

## Contexto

CSRF força o browser autenticado a emitir requests state-changing.
Defesas (tokens, SameSite, Origin) falham por misconfig, method override, JSON com content-types
permissivos e XSS que lê tokens. SameSite=Lax não cobre tudo (chrome changes, subdomain XSS).

## Variante

- **Bypass de checks GET** — muda ruído e o que entra no PDF.
- SameSite ajuda; não substitui token em API cookie-based. State change cross-site com sessão válida.

## Setup

Ativo mínimo. Duas identidades se for authz.
Restore point.

## Fluxo

1. Identifico ações sem token / com cookie session.
2. Monto PoC HTML em origem controlada de lab.
3. Testo SameSite, Origin/Referer validation bypasses.
4. Avalio content-type (text/plain JSON).
5. Meço impacto (mudança de e-mail, transfer).

## Sinal / query

```html
<form action="https://app.lab.local/api/settings/email" method="POST">
  <input name="email" value="attacker_80b458@lab.local">
</form>
<script>document.forms[0].submit()</script>
<!-- CSRF method-override: state change com cookie USER_A -->
```

## Pitfall

Login CSRF também importa. Não executo ações em contas alheias.

XSS/CSRF: preciso do sink e da condição de auth. alert(1) sem abuso de sessão é demo.

## Prova do lab

PoC HTML; request forjado; efeito na conta teste.

## Refs

- [OWASP CSRF Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)
- [PortSwigger — CSRF](https://portswigger.net/web-security/csrf)

## Relacionadas

- [X-HTTP-Method-Override](0164-client-csrf-method-override.md)
- [X-HTTP-Method-Override — hardening](0924-client-csrf-method-override--hardening.md)
- [clickjacking + CSRF](0170-client-csrf-clickjacking.md)
- [CORS reflection + CSRF](0169-client-csrf-cors.md)
- [JSON CSRF via text/plain](0163-client-csrf-json-csrf.md)
- [logout CSRF](0168-client-csrf-logout.md)