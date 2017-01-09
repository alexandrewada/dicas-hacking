# falta de validação aud/iss

## Leitura rápida

JWTs mal implementados permitem alg=none, confusão RS256/HS256, kid injection (SQL/path),
claims sensíveis sem validação de iss/aud/exp, e tokens eternamente válidos sem revogação.
Valido a biblioteca verificadora, não só o conteúdo do token.

## Foco

- Detalhe que pago pra ver: **Token de outro ambiente aceito**.
- Testo verify path na lib real. Claim admin:true sem verify não é bypass.

## Mãos na massa

1. Decodifico header/payload; mapeio claims.
2. Testo alg none e troca de algoritmo conforme biblioteca.
3. Avalio kid/jku/x5u se presentes (SSRF/file).
4. Verifico aud/iss/nbf/exp e clock skew.
5. Testo privilege claims e token sidejacking.

## Exemplo

```http
GET /api/v1/admin/users HTTP/1.1
Host: api.lab.local
Authorization: Bearer JWT_aud-iss_f2679e
# claim tamper / kid / aud — ver variante aud-iss
```

403 no gateway com 200 no origin — path direto e Host conforme ROE.

## Pitfall

Nem todo JWT 'sem exp' é explorável se houver store server-side.
Não exfiltro tokens de usuários reais — uso contas de teste.

## Detecção / remediação

Invalid signature spikes; impossible travel com tokens; denylist.

→ Bibliotecas atualizadas; enforce algorithm; short TTL + refresh rotation;
bind token a client quando possível; revogação.

## Prova

Token de teste manipulado; response privilegiada; libs/versão.

## Refs

- RFC 7519
- PortSwigger JWT
- OWASP JWT Cheat Sheet