# logout CSRF — hardening

Do PoC ao controle — logout CSRF.

## Risco

CSRF força o browser autenticado a emitir requests state-changing.
Defesas (tokens, SameSite, Origin) falham por misconfig, method override, JSON com content-types
permissivos e XSS que lê tokens. SameSite=Lax não cobre tudo (chrome changes, subdomain XSS).

## Controles desta variante

- Se não validar **DoS de sessão / fixation prep**, a nota fica genérica.
- SameSite ajuda; não substitui token em API cookie-based. State change cross-site com sessão válida.

## Camadas

1) Bloqueio imediato
2) Origin failures; CSRF token mismatch metrics.
3) Anti-CSRF tokens; SameSite=Strict/Lax consciente; Preferir Authorization header;
re-auth para ações críticas.
Reteste com o mesmo PoC — critério: a prova desta variante falha.

## PoC mínimo

```bash
# verificação pós-hardening logout
curl -sk -o /dev/null -w '%{http_code}\n' https://app.lab.local/logout/usr_01HZX \
  -H 'Cookie: session=USER_B'
# esperado 403 — tag 3749f8
```

## Armadilha

Login CSRF também importa. Não executo ações em contas alheias.

## Antes/depois

PoC HTML; request forjado; efeito na conta teste.

Aceite de risco só por escrito, com prazo.

## Refs

- OWASP CSRF
- PortSwigger CSRF