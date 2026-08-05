---
id: "0164"
categoria: "06-client"
familia: "client-csrf"
slug: "method-override"
angulo: "base"
mitre: ""
owasp: ""
tags: ["06-client", "client-csrf", "base"]
aliases: ["X-HTTP-Method-Override", "method-override"]
---

# X-HTTP-Method-Override

## Leitura rápida

CSRF força o browser autenticado a emitir requests state-changing.
Defesas (tokens, SameSite, Origin) falham por misconfig, method override, JSON com content-types
permissivos e XSS que lê tokens. SameSite=Lax não cobre tudo (chrome changes, subdomain XSS).

## Foco

- **Bypass de checks GET** — muda ruído e o que entra no PDF.
- SameSite ajuda; não substitui token em API cookie-based. State change cross-site com sessão válida.

## Mãos na massa

1. Identifico ações sem token / com cookie session.
2. Monto PoC HTML em origem controlada de lab.
3. Testo SameSite, Origin/Referer validation bypasses.
4. Avalio content-type (text/plain JSON).
5. Meço impacto (mudança de e-mail, transfer).

## Sinal / query

```html
<form action="https://app.lab.local/api/settings/email" method="POST">
  <input name="email" value="attacker_9280c5@lab.local">
</form>
<script>document.forms[0].submit()</script>
<!-- CSRF method-override: state change com cookie USER_A -->
```

XSS/CSRF: preciso do sink e da condição de auth. alert(1) sem abuso de sessão é demo.

## Pitfall

Login CSRF também importa. Não executo ações em contas alheias.

## Detecção / remediação

Origin failures; CSRF token mismatch metrics.

→ Anti-CSRF tokens; SameSite=Strict/Lax consciente; Preferir Authorization header;
re-auth para ações críticas.

## Prova

PoC HTML; request forjado; efeito na conta teste.

## Refs

- [OWASP CSRF Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)
- [PortSwigger — CSRF](https://portswigger.net/web-security/csrf)

## Relacionadas

- [X-HTTP-Method-Override — lab](0544-client-csrf-method-override--lab.md)
- [X-HTTP-Method-Override — hardening](0924-client-csrf-method-override--hardening.md)
- [clickjacking + CSRF](0170-client-csrf-clickjacking.md)
- [CORS reflection + CSRF](0169-client-csrf-cors.md)
- [JSON CSRF via text/plain](0163-client-csrf-json-csrf.md)
- [logout CSRF](0168-client-csrf-logout.md)