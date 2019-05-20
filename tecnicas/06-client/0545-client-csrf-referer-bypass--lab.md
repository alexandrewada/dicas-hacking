# Referer opcional/vazio — lab

Lab só pra Referer opcional/vazio. Se não reproduz isolado, não confio no finding de prod.

## Contexto

CSRF força o browser autenticado a emitir requests state-changing.
Defesas (tokens, SameSite, Origin) falham por misconfig, method override, JSON com content-types
permissivos e XSS que lê tokens. SameSite=Lax não cobre tudo (chrome changes, subdomain XSS).

## Variante

- **Policy frouxa.** Sem isso o playbook da família mente.
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

## Exemplo

```html
<form action="https://app.lab.local/api/settings/email" method="POST">
  <input name="email" value="attacker_c759a6@lab.local">
</form>
<script>document.forms[0].submit()</script>
<!-- CSRF referer-bypass: state change com cookie USER_A -->
```

## Pitfall

Login CSRF também importa. Não executo ações em contas alheias.

CSP bypass só se atravesso a política atual do alvo, não CSP de lab antiga.

## Prova do lab

PoC HTML; request forjado; efeito na conta teste.

## Refs

- OWASP CSRF
- PortSwigger CSRF