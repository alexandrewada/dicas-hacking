---
id: "0548"
categoria: "06-client"
familia: "client-csrf"
slug: "logout"
angulo: "lab"
mitre: "T1185"
owasp: ""
tags: ["06-client", "client-csrf", "lab", "t1185"]
aliases: ["logout CSRF", "logout", "logout-lab"]
---

# logout CSRF — lab

Critério: outro analista fecha sozinho com esta nota.

## Contexto

CSRF força o browser autenticado a emitir requests state-changing.
Defesas (tokens, SameSite, Origin) falham por misconfig, method override, JSON com content-types
permissivos e XSS que lê tokens. SameSite=Lax não cobre tudo (chrome changes, subdomain XSS).

## Variante

- Se não validar **DoS de sessão / fixation prep**, a nota fica genérica.
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
  <input name="email" value="attacker_d3a155@lab.local">
</form>
<script>document.forms[0].submit()</script>
<!-- CSRF logout: state change com cookie USER_A -->
```

## Pitfall

Login CSRF também importa. Não executo ações em contas alheias.

Não persisto payload em produção sem janela e plano de purge.

## Prova do lab

PoC HTML; request forjado; efeito na conta teste.

## Refs

- [MITRE ATT&CK T1185](https://attack.mitre.org/techniques/T1185/)
- [OWASP CSRF Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)
- [PortSwigger — CSRF](https://portswigger.net/web-security/csrf)

## Relacionadas

- [logout CSRF](0168-client-csrf-logout.md)
- [logout CSRF — hardening](0928-client-csrf-logout--hardening.md)
- [clickjacking + CSRF](0170-client-csrf-clickjacking.md)
- [CORS reflection + CSRF](0169-client-csrf-cors.md)
- [JSON CSRF via text/plain](0163-client-csrf-json-csrf.md)
- [X-HTTP-Method-Override](0164-client-csrf-method-override.md)