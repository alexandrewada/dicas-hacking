---
id: "0162"
categoria: "06-client"
familia: "client-csrf"
slug: "samesite"
angulo: "base"
mitre: "T1185"
owasp: ""
tags: ["06-client", "client-csrf", "base", "t1185"]
aliases: ["SameSite=None sem Secure", "samesite"]
---

# SameSite=None sem Secure

**A01 Broken Access Control** · `T1185 Browser Session Hijacking (adjunto)`

CSRF força o browser autenticado a emitir requests state-changing.
Defesas (tokens, SameSite, Origin) falham por misconfig, method override, JSON com content-types
permissivos e XSS que lê tokens. SameSite=Lax não cobre tudo (chrome changes, subdomain XSS).

**Variante:** **Quebra defesa.** Sem isso o playbook da família mente. SameSite ajuda; não substitui token em API cookie-based. State change cross-site com sessão válida.

**Método**

1. Identifico ações sem token / com cookie session.
2. Monto PoC HTML em origem controlada de lab.
3. Testo SameSite, Origin/Referer validation bypasses.
4. Avalio content-type (text/plain JSON).
5. Meço impacto (mudança de e-mail, transfer).

## No lab ficou assim

```html
<form action="https://app.lab.local/api/settings/email" method="POST">
  <input name="email" value="attacker_bc3aec@lab.local">
</form>
<script>document.forms[0].submit()</script>
<!-- CSRF samesite: state change com cookie USER_A -->
```

**Freio:** Login CSRF também importa. Não executo ações em contas alheias.

SameSite=None sem Secure: se não reproduz efeito (authz/dado/exec), não infla severidade. Referência de sinal: Origin failures; CSRF token mismatch metrics.

Detecto via: Origin failures; CSRF token mismatch metrics.

Corrijo com: Anti-CSRF tokens; SameSite=Strict/Lax consciente; Preferir Authorization header;
re-auth para ações críticas.

Levo no report: PoC HTML; request forjado; efeito na conta teste.

## Refs

- [MITRE ATT&CK T1185](https://attack.mitre.org/techniques/T1185/)
- [OWASP CSRF Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)
- [PortSwigger — CSRF](https://portswigger.net/web-security/csrf)

## Relacionadas

- [SameSite=None sem Secure — lab](0542-client-csrf-samesite--lab.md)
- [SameSite=None sem Secure — hardening](0922-client-csrf-samesite--hardening.md)
- [clickjacking + CSRF](0170-client-csrf-clickjacking.md)
- [CORS reflection + CSRF](0169-client-csrf-cors.md)
- [JSON CSRF via text/plain](0163-client-csrf-json-csrf.md)
- [logout CSRF](0168-client-csrf-logout.md)