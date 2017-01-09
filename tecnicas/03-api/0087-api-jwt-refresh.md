# refresh token fixation/reuse

`T1550 Use Alternate Authentication Material`

## Por que importa

JWTs mal implementados permitem alg=none, confusão RS256/HS256, kid injection (SQL/path),
claims sensíveis sem validação de iss/aud/exp, e tokens eternamente válidos sem revogação.
Valido a biblioteca verificadora, não só o conteúdo do token.

## Variante

- **Reuse detection ausente** — muda ruído e o que entra no PDF.
- Testo verify path na lib real. Claim admin:true sem verify não é bypass.

## Passo a passo

1. Decodifico header/payload; mapeio claims.
2. Testo alg none e troca de algoritmo conforme biblioteca.
3. Avalio kid/jku/x5u se presentes (SSRF/file).
4. Verifico aud/iss/nbf/exp e clock skew.
5. Testo privilege claims e token sidejacking.

## PoC mínimo

```http
GET /api/v1/admin/users HTTP/1.1
Host: api.lab.local
Authorization: Bearer JWT_refresh_1a0514
# claim tamper / kid / aud — ver variante refresh
```

## Nota de operador

403 no gateway com 200 no origin — path direto e Host conforme ROE.

## Armadilha

Nem todo JWT 'sem exp' é explorável se houver store server-side.
Não exfiltro tokens de usuários reais — uso contas de teste.

Antes de Critical em refresh token fixation/reuse, confiro se a telemetria que eu cobraria reagiria — Invalid signature spikes; impossible travel com tokens; denylist.

## Depois

Detecção — Invalid signature spikes; impossible travel com tokens; denylist.

Remediação — Bibliotecas atualizadas; enforce algorithm; short TTL + refresh rotation;
bind token a client quando possível; revogação.

No PDF — Token de teste manipulado; response privilegiada; libs/versão.

## Refs

- RFC 7519
- PortSwigger JWT
- OWASP JWT Cheat Sheet