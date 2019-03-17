# JSON CSRF via text/plain

## Leitura rápida

CSRF força o browser autenticado a emitir requests state-changing.
Defesas (tokens, SameSite, Origin) falham por misconfig, method override, JSON com content-types
permissivos e XSS que lê tokens. SameSite=Lax não cobre tudo (chrome changes, subdomain XSS).

## Foco

- **Flash legado / nav quirks.** Sem isso o playbook da família mente.
- SameSite ajuda; não substitui token em API cookie-based. State change cross-site com sessão válida.

## Mãos na massa

1. Identifico ações sem token / com cookie session.
2. Monto PoC HTML em origem controlada de lab.
3. Testo SameSite, Origin/Referer validation bypasses.
4. Avalio content-type (text/plain JSON).
5. Meço impacto (mudança de e-mail, transfer).

## Exemplo

```html
<form action="https://app.lab.local/api/settings/email" method="POST">
  <input name="email" value="attacker_c1cae4@lab.local">
</form>
<script>document.forms[0].submit()</script>
<!-- CSRF json-csrf: state change com cookie USER_A -->
```

CSP bypass só se atravesso a política atual do alvo, não CSP de lab antiga.

## Pitfall

Login CSRF também importa. Não executo ações em contas alheias.

## Detecção / remediação

Origin failures; CSRF token mismatch metrics.

→ Anti-CSRF tokens; SameSite=Strict/Lax consciente; Preferir Authorization header;
re-auth para ações críticas.

## Prova

PoC HTML; request forjado; efeito na conta teste.

## Refs

- OWASP CSRF
- PortSwigger CSRF