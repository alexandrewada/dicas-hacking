---
id: "0547"
categoria: "06-client"
familia: "client-csrf"
slug: "websocket"
angulo: "lab"
mitre: "T1185"
owasp: ""
tags: ["06-client", "client-csrf", "lab", "t1185"]
aliases: ["CSWSH", "websocket", "websocket-lab"]
---

# CSWSH — lab

Lab só pra CSWSH. Se não reproduz isolado, não confio no finding de prod.

## Contexto

CSRF força o browser autenticado a emitir requests state-changing.
Defesas (tokens, SameSite, Origin) falham por misconfig, method override, JSON com content-types
permissivos e XSS que lê tokens. SameSite=Lax não cobre tudo (chrome changes, subdomain XSS).

## Variante

- Se não validar **WebSocket CSRF**, a nota fica genérica.
- SameSite ajuda; não substitui token em API cookie-based. State change cross-site com sessão válida.

## Setup

VM/conta throwaway na versão parecida.
Snapshot antes.
Cleanup escrito antes de explorar.

## Fluxo

1. Identifico ações sem token / com cookie session.
2. Monto PoC HTML em origem controlada de lab.
3. Testo SameSite, Origin/Referer validation bypasses.
4. Avalio content-type (text/plain JSON).
5. Meço impacto (mudança de e-mail, transfer).

## Sinal / query

```html
<form action="https://app.lab.local/api/settings/email" method="POST">
  <input name="email" value="attacker_2d2b05@lab.local">
</form>
<script>document.forms[0].submit()</script>
<!-- CSRF websocket: state change com cookie USER_A -->
```

## Pitfall

Login CSRF também importa. Não executo ações em contas alheias.

XSS/CSRF: preciso do sink e da condição de auth. alert(1) sem abuso de sessão é demo.

## Prova do lab

PoC HTML; request forjado; efeito na conta teste.

## Refs

- [MITRE ATT&CK T1185](https://attack.mitre.org/techniques/T1185/)
- [OWASP CSRF Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)
- [PortSwigger — CSRF](https://portswigger.net/web-security/csrf)

## Relacionadas

- [CSWSH](0167-client-csrf-websocket.md)
- [CSWSH — hardening](0927-client-csrf-websocket--hardening.md)
- [clickjacking + CSRF](0170-client-csrf-clickjacking.md)
- [CORS reflection + CSRF](0169-client-csrf-cors.md)
- [JSON CSRF via text/plain](0163-client-csrf-json-csrf.md)
- [logout CSRF](0168-client-csrf-logout.md)