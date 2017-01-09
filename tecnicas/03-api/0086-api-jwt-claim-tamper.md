# tampering de role/admin

## Contexto

JWTs mal implementados permitem alg=none, confusão RS256/HS256, kid injection (SQL/path),
claims sensíveis sem validação de iss/aud/exp, e tokens eternamente válidos sem revogação.
Valido a biblioteca verificadora, não só o conteúdo do token.

## Detalhe

- Se não validar **Sem verificação de assinatura efetiva**, a nota fica genérica.
- Testo verify path na lib real. Claim admin:true sem verify não é bypass.

## Execução

1. Decodifico header/payload; mapeio claims.
2. Testo alg none e troca de algoritmo conforme biblioteca.
3. Avalio kid/jku/x5u se presentes (SSRF/file).
4. Verifico aud/iss/nbf/exp e clock skew.
5. Testo privilege claims e token sidejacking.

## Sinal / query

```http
GET /api/v1/admin/users HTTP/1.1
Host: api.lab.local
Authorization: Bearer JWT_claim-tamper_777853
# claim tamper / kid / aud — ver variante claim-tamper
```

## OpSec

Nem todo JWT 'sem exp' é explorável se houver store server-side.

## Cuidados

Nem todo JWT 'sem exp' é explorável se houver store server-side.
Não exfiltro tokens de usuários reais — uso contas de teste.

## Fechamento

| | |
|---|---|
| Detecção | Invalid signature spikes; impossible travel com tokens; denylist. |
| Remediação | Bibliotecas atualizadas; enforce algorithm; short TTL + refresh rotation;
bind token a client quando possível; revogação. |
| Evidência | Token de teste manipulado; response privilegiada; libs/versão. |

## Refs

- RFC 7519
- PortSwigger JWT
- OWASP JWT Cheat Sheet