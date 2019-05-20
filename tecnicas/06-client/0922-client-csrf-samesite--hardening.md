# SameSite=None sem Secure — hardening

Do PoC ao controle — SameSite=None sem Secure.

## Risco

CSRF força o browser autenticado a emitir requests state-changing.
Defesas (tokens, SameSite, Origin) falham por misconfig, method override, JSON com content-types
permissivos e XSS que lê tokens. SameSite=Lax não cobre tudo (chrome changes, subdomain XSS).

## Controles desta variante

- **Quebra defesa.** Sem isso o playbook da família mente.
- SameSite ajuda; não substitui token em API cookie-based. State change cross-site com sessão válida.

## Camadas

Hotfix: quebra a exploração direta de SameSite=None sem Secure.
Detectivo: Origin failures; CSRF token mismatch metrics.
Estrutural: Anti-CSRF tokens; SameSite=Strict/Lax consciente; Preferir Authorization header;
re-auth para ações críticas.

## No lab ficou assim

```bash
# verificação pós-hardening samesite
curl -sk -o /dev/null -w '%{http_code}\n' https://app.lab.local/samesite/a1b2c3d4-e5f6-7890-abcd-ef1234567890 \
  -H 'Cookie: session=USER_B'
# esperado 403 — tag 6305ee
```

## Armadilha

Login CSRF também importa. Não executo ações em contas alheias.

## Antes/depois

PoC HTML; request forjado; efeito na conta teste.

Aceite de risco só por escrito, com prazo.

## Refs

- OWASP CSRF
- PortSwigger CSRF