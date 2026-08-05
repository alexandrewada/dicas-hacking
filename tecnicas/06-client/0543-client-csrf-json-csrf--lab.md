---
id: "0543"
categoria: "06-client"
familia: "client-csrf"
slug: "json-csrf"
angulo: "lab"
mitre: ""
owasp: ""
tags: ["06-client", "client-csrf", "lab"]
aliases: ["JSON CSRF via text/plain", "json-csrf", "json-csrf-lab"]
---

# JSON CSRF via text/plain — lab

Critério: outro analista fecha sozinho com esta nota.

## Contexto

CSRF força o browser autenticado a emitir requests state-changing.
Defesas (tokens, SameSite, Origin) falham por misconfig, method override, JSON com content-types
permissivos e XSS que lê tokens. SameSite=Lax não cobre tudo (chrome changes, subdomain XSS).

## Variante

- **Flash legado / nav quirks.** Sem isso o playbook da família mente.
- SameSite ajuda; não substitui token em API cookie-based. State change cross-site com sessão válida.

## Setup

Espelho do alvo. Sem WAF/EDR às vezes — anoto o delta.

## Fluxo

1. Identifico ações sem token / com cookie session.
2. Monto PoC HTML em origem controlada de lab.
3. Testo SameSite, Origin/Referer validation bypasses.
4. Avalio content-type (text/plain JSON).
5. Meço impacto (mudança de e-mail, transfer).

## PoC mínimo

```html
<form action="https://app.lab.local/api/settings/email" method="POST">
  <input name="email" value="attacker_4a2fae@lab.local">
</form>
<script>document.forms[0].submit()</script>
<!-- CSRF json-csrf: state change com cookie USER_A -->
```

## Pitfall

Login CSRF também importa. Não executo ações em contas alheias.

CSP bypass só se atravesso a política atual do alvo, não CSP de lab antiga.

## Prova do lab

PoC HTML; request forjado; efeito na conta teste.

## Refs

- [OWASP CSRF Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)
- [PortSwigger — CSRF](https://portswigger.net/web-security/csrf)

## Relacionadas

- [JSON CSRF via text/plain](0163-client-csrf-json-csrf.md)
- [JSON CSRF via text/plain — hardening](0923-client-csrf-json-csrf--hardening.md)
- [clickjacking + CSRF](0170-client-csrf-clickjacking.md)
- [CORS reflection + CSRF](0169-client-csrf-cors.md)
- [logout CSRF](0168-client-csrf-logout.md)
- [X-HTTP-Method-Override](0164-client-csrf-method-override.md)