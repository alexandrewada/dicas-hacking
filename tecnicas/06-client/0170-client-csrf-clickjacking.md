# clickjacking + CSRF

**A01 Broken Access Control** · `T1185 Browser Session Hijacking (adjunto)`

CSRF força o browser autenticado a emitir requests state-changing.
Defesas (tokens, SameSite, Origin) falham por misconfig, method override, JSON com content-types
permissivos e XSS que lê tokens. SameSite=Lax não cobre tudo (chrome changes, subdomain XSS).

**Variante:** **UI redress.** Sem isso o playbook da família mente. SameSite ajuda; não substitui token em API cookie-based. State change cross-site com sessão válida.

**Método**

1. Identifico ações sem token / com cookie session.
2. Monto PoC HTML em origem controlada de lab.
3. Testo SameSite, Origin/Referer validation bypasses.
4. Avalio content-type (text/plain JSON).
5. Meço impacto (mudança de e-mail, transfer).

## No lab ficou assim

```html
<form action="https://app.lab.local/api/settings/email" method="POST">
  <input name="email" value="attacker_a15684@lab.local">
</form>
<script>document.forms[0].submit()</script>
<!-- CSRF clickjacking: state change com cookie USER_A -->
```

**Freio:** Login CSRF também importa. Não executo ações em contas alheias.

Antes de Critical em clickjacking + CSRF, confiro se a telemetria que eu cobraria reagiria — Origin failures; CSRF token mismatch metrics.

Detecto via: Origin failures; CSRF token mismatch metrics.

Corrijo com: Anti-CSRF tokens; SameSite=Strict/Lax consciente; Preferir Authorization header;
re-auth para ações críticas.

Levo no report: PoC HTML; request forjado; efeito na conta teste.

Refs: OWASP CSRF, PortSwigger CSRF