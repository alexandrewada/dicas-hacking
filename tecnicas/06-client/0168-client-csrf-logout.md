---
id: "0168"
categoria: "06-client"
familia: "client-csrf"
slug: "logout"
angulo: "base"
mitre: "T1185"
owasp: ""
tags: ["06-client", "client-csrf", "base", "t1185"]
aliases: ["logout CSRF", "logout"]
---

# logout CSRF

**A01 Broken Access Control** · `T1185 Browser Session Hijacking (adjunto)`

CSRF força o browser autenticado a emitir requests state-changing.
Defesas (tokens, SameSite, Origin) falham por misconfig, method override, JSON com content-types
permissivos e XSS que lê tokens. SameSite=Lax não cobre tudo (chrome changes, subdomain XSS).

**Variante:** Se não validar **DoS de sessão / fixation prep**, a nota fica genérica. SameSite ajuda; não substitui token em API cookie-based. State change cross-site com sessão válida.

**Método**

1. Identifico ações sem token / com cookie session.
2. Monto PoC HTML em origem controlada de lab.
3. Testo SameSite, Origin/Referer validation bypasses.
4. Avalio content-type (text/plain JSON).
5. Meço impacto (mudança de e-mail, transfer).

## Exemplo

```html
<form action="https://app.lab.local/api/settings/email" method="POST">
  <input name="email" value="attacker_78379c@lab.local">
</form>
<script>document.forms[0].submit()</script>
<!-- CSRF logout: state change com cookie USER_A -->
```

**Freio:** Login CSRF também importa. Não executo ações em contas alheias.

Antes de Critical em logout CSRF, confiro se a telemetria que eu cobraria reagiria — Origin failures; CSRF token mismatch metrics.

Detecto via: Origin failures; CSRF token mismatch metrics.

Corrijo com: Anti-CSRF tokens; SameSite=Strict/Lax consciente; Preferir Authorization header;
re-auth para ações críticas.

Levo no report: PoC HTML; request forjado; efeito na conta teste.

## Refs

- [MITRE ATT&CK T1185](https://attack.mitre.org/techniques/T1185/)
- [OWASP CSRF Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)
- [PortSwigger — CSRF](https://portswigger.net/web-security/csrf)

## Relacionadas

- [logout CSRF — lab](0548-client-csrf-logout--lab.md)
- [logout CSRF — hardening](0928-client-csrf-logout--hardening.md)
- [clickjacking + CSRF](0170-client-csrf-clickjacking.md)
- [CORS reflection + CSRF](0169-client-csrf-cors.md)
- [JSON CSRF via text/plain](0163-client-csrf-json-csrf.md)
- [X-HTTP-Method-Override](0164-client-csrf-method-override.md)