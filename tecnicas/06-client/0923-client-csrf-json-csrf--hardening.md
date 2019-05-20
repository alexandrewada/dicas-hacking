# JSON CSRF via text/plain — hardening

Do PoC ao controle — JSON CSRF via text/plain.

## Risco

CSRF força o browser autenticado a emitir requests state-changing.
Defesas (tokens, SameSite, Origin) falham por misconfig, method override, JSON com content-types
permissivos e XSS que lê tokens. SameSite=Lax não cobre tudo (chrome changes, subdomain XSS).

## Controles desta variante

- **Flash legado / nav quirks.** Sem isso o playbook da família mente.
- SameSite ajuda; não substitui token em API cookie-based. State change cross-site com sessão válida.

## Camadas

1) Bloqueio imediato
2) Origin failures; CSRF token mismatch metrics.
3) Anti-CSRF tokens; SameSite=Strict/Lax consciente; Preferir Authorization header;
re-auth para ações críticas.
Reteste com o mesmo PoC — critério: a prova desta variante falha.

## PoC mínimo

```text
checklist json-csrf:
- [ ] controle preventivo ativo
- [ ] telemetria cobre o PoC
- [ ] reteste com mesma prova (adc219) falha
```

## Armadilha

Login CSRF também importa. Não executo ações em contas alheias.

## Antes/depois

PoC HTML; request forjado; efeito na conta teste.

Aceite de risco só por escrito, com prazo.

## Refs

- OWASP CSRF
- PortSwigger CSRF