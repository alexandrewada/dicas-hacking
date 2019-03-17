# CSWSH

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
  <input name="email" value="attacker_460106@lab.local">
</form>
<script>document.forms[0].submit()</script>
<!-- CSRF websocket: state change com cookie USER_A -->
```

## Diferencial desta nota

- Se não validar **WebSocket CSRF**, a nota fica genérica.
- SameSite ajuda; não substitui token em API cookie-based. State change cross-site com sessão válida.

Falso amigo em CSWSH: UI/log gritam, impacto não. Exijo Origin failures.

## Onde já errei

Login CSRF também importa. Não executo ações em contas alheias.

XSS/CSRF: preciso do sink e da condição de auth. alert(1) sem abuso de sessão é demo.

## Entrega

- blue: Origin failures; CSRF token mismatch metrics.
- fix: Anti-CSRF tokens; SameSite=Strict/Lax consciente; Preferir Authorization header;
re-auth para ações críticas.
- proof: PoC HTML; request forjado; efeito na conta teste.

## Refs

- OWASP CSRF
- PortSwigger CSRF