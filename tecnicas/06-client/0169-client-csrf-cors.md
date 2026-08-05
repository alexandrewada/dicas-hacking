---
id: "0169"
categoria: "06-client"
familia: "client-csrf"
slug: "cors"
angulo: "base"
mitre: "T1185"
owasp: ""
tags: ["06-client", "client-csrf", "base", "t1185"]
aliases: ["CORS reflection + CSRF", "cors"]
---

# CORS reflection + CSRF

**A01 Broken Access Control** · `T1185 Browser Session Hijacking (adjunto)`

CSRF força o browser autenticado a emitir requests state-changing.
Defesas (tokens, SameSite, Origin) falham por misconfig, method override, JSON com content-types
permissivos e XSS que lê tokens. SameSite=Lax não cobre tudo (chrome changes, subdomain XSS).

**Variante:** Se não validar **Amplifica impacto**, a nota fica genérica. SameSite ajuda; não substitui token em API cookie-based. State change cross-site com sessão válida. Origin refletido + credentials. Read autenticado de origem atacante — não só ACAO *.

**Método**

1. Identifico ações sem token / com cookie session.
2. Monto PoC HTML em origem controlada de lab.
3. Testo SameSite, Origin/Referer validation bypasses.
4. Avalio content-type (text/plain JSON).
5. Meço impacto (mudança de e-mail, transfer).

## PoC mínimo

```html
<form action="https://app.lab.local/api/settings/email" method="POST">
  <input name="email" value="attacker_1b1c4d@lab.local">
</form>
<script>document.forms[0].submit()</script>
<!-- CSRF cors: state change com cookie USER_A -->
```

**Freio:** Login CSRF também importa. Não executo ações em contas alheias.

Já abri High demais em CORS reflection + CSRF por sintoma sem efeito. Cruzei com: Origin failures; CSRF token mismatch metrics. Sem side-effect, baixo.

Detecto via: Origin failures; CSRF token mismatch metrics.

Corrijo com: Anti-CSRF tokens; SameSite=Strict/Lax consciente; Preferir Authorization header;
re-auth para ações críticas.

Levo no report: PoC HTML; request forjado; efeito na conta teste.

## Refs

- [MITRE ATT&CK T1185](https://attack.mitre.org/techniques/T1185/)
- [OWASP CSRF Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)
- [PortSwigger — CSRF](https://portswigger.net/web-security/csrf)

## Relacionadas

- [CORS reflection + CSRF — lab](0549-client-csrf-cors--lab.md)
- [CORS reflection + CSRF — hardening](0929-client-csrf-cors--hardening.md)
- [clickjacking + CSRF](0170-client-csrf-clickjacking.md)
- [JSON CSRF via text/plain](0163-client-csrf-json-csrf.md)
- [logout CSRF](0168-client-csrf-logout.md)
- [X-HTTP-Method-Override](0164-client-csrf-method-override.md)