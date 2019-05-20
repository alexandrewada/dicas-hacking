# XSS em subdomínio → CSRF — lab

Sandbox throwaway — XSS em subdomínio → CSRF sem ruído de cliente.

## Contexto

CSRF força o browser autenticado a emitir requests state-changing.
Defesas (tokens, SameSite, Origin) falham por misconfig, method override, JSON com content-types
permissivos e XSS que lê tokens. SameSite=Lax não cobre tudo (chrome changes, subdomain XSS).

## Variante

- Se não validar **Cookie scoped parents**, a nota fica genérica.
- SameSite ajuda; não substitui token em API cookie-based. State change cross-site com sessão válida.
- Sink + contexto + cookie flags. Encadeio até ação autenticada ou token se HttpOnly falhar.

## Setup

Ativo mínimo. Duas identidades se for authz.
Restore point.

## Fluxo

1. Identifico ações sem token / com cookie session.
2. Monto PoC HTML em origem controlada de lab.
3. Testo SameSite, Origin/Referer validation bypasses.
4. Avalio content-type (text/plain JSON).
5. Meço impacto (mudança de e-mail, transfer).

## No lab ficou assim

```html
<form action="https://app.lab.local/api/settings/email" method="POST">
  <input name="email" value="attacker_402a24@lab.local">
</form>
<script>document.forms[0].submit()</script>
<!-- CSRF subdomain: state change com cookie USER_A -->
```

## Pitfall

Login CSRF também importa. Não executo ações em contas alheias.

Não persisto payload em produção sem janela e plano de purge.

## Prova do lab

PoC HTML; request forjado; efeito na conta teste.

## Refs

- OWASP CSRF
- PortSwigger CSRF