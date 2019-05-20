# Referer opcional/vazio — hardening

Do PoC ao controle — Referer opcional/vazio.

## Risco

CSRF força o browser autenticado a emitir requests state-changing.
Defesas (tokens, SameSite, Origin) falham por misconfig, method override, JSON com content-types
permissivos e XSS que lê tokens. SameSite=Lax não cobre tudo (chrome changes, subdomain XSS).

## Controles desta variante

- **Policy frouxa.** Sem isso o playbook da família mente.
- SameSite ajuda; não substitui token em API cookie-based. State change cross-site com sessão válida.

## Camadas

Hotfix: quebra a exploração direta de Referer opcional/vazio.
Detectivo: Origin failures; CSRF token mismatch metrics.
Estrutural: Anti-CSRF tokens; SameSite=Strict/Lax consciente; Preferir Authorization header;
re-auth para ações críticas.

## Exemplo

```text
antes: controle ausente para referer-bypass
depois: ownership check / deny default em TARGET
verificação: PoC 7a719d retorna 403/blocked
reteste USER_A vs USER_B
```

## Armadilha

Login CSRF também importa. Não executo ações em contas alheias.

## Antes/depois

PoC HTML; request forjado; efeito na conta teste.

Aceite de risco só por escrito, com prazo.

## Refs

- OWASP CSRF
- PortSwigger CSRF