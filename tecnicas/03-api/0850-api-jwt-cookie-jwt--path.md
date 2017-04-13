# JWT em cookie sem flags — path

JWT em cookie sem flags como pivô. Path curto > monte de finding isolado.

## Papel

JWTs mal implementados permitem alg=none, confusão RS256/HS256, kid injection (SQL/path),
claims sensíveis sem validação de iss/aud/exp, e tokens eternamente válidos sem revogação.
Valido a biblioteca verificadora, não só o conteúdo do token.

## Por que pivota

- Detalhe que pago pra ver: **XSS → account takeover**.
- Testo verify path na lib real. Claim admin:true sem verify não é bypass.

## Cadeia

1. Entrada (escopo)
2. Pivô: JWT em cookie sem flags
3. Objetivo do ROE
4. Persistência só se pedido, com kill-switch

## Execução do pivô

1. Decodifico header/payload; mapeio claims.
2. Testo alg none e troca de algoritmo conforme biblioteca.
3. Avalio kid/jku/x5u se presentes (SSRF/file).
4. Verifico aud/iss/nbf/exp e clock skew.
5. Testo privilege claims e token sidejacking.

## Exemplo

```http
GET /api/v1/admin/users HTTP/1.1
Host: api.lab.local
Authorization: Bearer JWT_cookie-jwt_6c72f3
# claim tamper / kid / aud — ver variante cookie-jwt
```

## Freio

Nem todo JWT 'sem exp' é explorável se houver store server-side.
Não exfiltro tokens de usuários reais — uso contas de teste.

## No caminho

Detectar: Invalid signature spikes; impossible travel com tokens; denylist.

Remediar: Bibliotecas atualizadas; enforce algorithm; short TTL + refresh rotation;
bind token a client quando possível; revogação.

## Prova

Token de teste manipulado; response privilegiada; libs/versão.

403 no gateway com 200 no origin — path direto e Host conforme ROE.

## Refs

- RFC 7519
- PortSwigger JWT
- OWASP JWT Cheat Sheet