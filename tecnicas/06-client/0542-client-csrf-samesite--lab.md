# SameSite=None sem Secure — lab

Lab só pra SameSite=None sem Secure. Se não reproduz isolado, não confio no finding de prod.

## Contexto

CSRF força o browser autenticado a emitir requests state-changing.
Defesas (tokens, SameSite, Origin) falham por misconfig, method override, JSON com content-types
permissivos e XSS que lê tokens. SameSite=Lax não cobre tudo (chrome changes, subdomain XSS).

## Variante

- **Quebra defesa.** Sem isso o playbook da família mente.
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

## No lab ficou assim

```html
<form action="https://app.lab.local/api/settings/email" method="POST">
  <input name="email" value="attacker_317b86@lab.local">
</form>
<script>document.forms[0].submit()</script>
<!-- CSRF samesite: state change com cookie USER_A -->
```

## Pitfall

Login CSRF também importa. Não executo ações em contas alheias.

Não persisto payload em produção sem janela e plano de purge.

## Prova do lab

PoC HTML; request forjado; efeito na conta teste.

## Refs

- OWASP CSRF
- PortSwigger CSRF