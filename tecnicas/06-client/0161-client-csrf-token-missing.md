---
id: "0161"
categoria: "06-client"
familia: "client-csrf"
slug: "token-missing"
angulo: "base"
mitre: "T1185"
owasp: ""
tags: ["06-client", "client-csrf", "base", "t1185"]
aliases: ["ausência total de token", "token-missing"]
---

# ausência total de token

**A01 Broken Access Control** · `T1185 Browser Session Hijacking (adjunto)`

## Contexto

CSRF força o browser autenticado a emitir requests state-changing.
Defesas (tokens, SameSite, Origin) falham por misconfig, method override, JSON com content-types
permissivos e XSS que lê tokens. SameSite=Lax não cobre tudo (chrome changes, subdomain XSS).

## Como eu faço

1. Identifico ações sem token / com cookie session.
2. Monto PoC HTML em origem controlada de lab.
3. Testo SameSite, Origin/Referer validation bypasses.
4. Avalio content-type (text/plain JSON).
5. Meço impacto (mudança de e-mail, transfer).

## PoC mínimo

```html
<form action="https://app.lab.local/api/settings/email" method="POST">
  <input name="email" value="attacker_6c0d4e@lab.local">
</form>
<script>document.forms[0].submit()</script>
<!-- CSRF token-missing: state change com cookie USER_A -->
```

## Diferencial desta nota

- **Finding clássico.** Sem isso o playbook da família mente.
- SameSite ajuda; não substitui token em API cookie-based. State change cross-site com sessão válida.

Antes de Critical em ausência total de token, confiro se a telemetria que eu cobraria reagiria — Origin failures; CSRF token mismatch metrics.

## Onde já errei

Login CSRF também importa. Não executo ações em contas alheias.

Não persisto payload em produção sem janela e plano de purge.

## Entrega

- blue: Origin failures; CSRF token mismatch metrics.
- fix: Anti-CSRF tokens; SameSite=Strict/Lax consciente; Preferir Authorization header;
re-auth para ações críticas.
- proof: PoC HTML; request forjado; efeito na conta teste.

## Refs

- [MITRE ATT&CK T1185](https://attack.mitre.org/techniques/T1185/)
- [OWASP CSRF Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)
- [PortSwigger — CSRF](https://portswigger.net/web-security/csrf)

## Relacionadas

- [ausência total de token — lab](0541-client-csrf-token-missing--lab.md)
- [ausência total de token — hardening](0921-client-csrf-token-missing--hardening.md)
- [clickjacking + CSRF](0170-client-csrf-clickjacking.md)
- [CORS reflection + CSRF](0169-client-csrf-cors.md)
- [JSON CSRF via text/plain](0163-client-csrf-json-csrf.md)
- [logout CSRF](0168-client-csrf-logout.md)
- [isAdmin/role elevation (path)](../03-api/0061-api-mass-assignment-role-flag.md)