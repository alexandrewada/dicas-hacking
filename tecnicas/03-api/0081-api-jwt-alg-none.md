# JWT com alg=none

**A07 Identification and Authentication Failures** · `T1550 Use Alternate Authentication Material`

## Contexto

JWTs mal implementados permitem alg=none, confusão RS256/HS256, kid injection (SQL/path),
claims sensíveis sem validação de iss/aud/exp, e tokens eternamente válidos sem revogação.
Valido a biblioteca verificadora, não só o conteúdo do token.

## Como eu faço

1. Decodifico header/payload; mapeio claims.
2. Testo alg none e troca de algoritmo conforme biblioteca.
3. Avalio kid/jku/x5u se presentes (SSRF/file).
4. Verifico aud/iss/nbf/exp e clock skew.
5. Testo privilege claims e token sidejacking.

## PoC mínimo

```http
GET /api/me HTTP/1.1
Host: api.lab.local
Authorization: Bearer eyJhbGciOiJub25lIn0.eyJzdWIiOiJUSER_AIiwicm9sZSI6ImFkbWluIn0.
# se 200 com role admin sem verify → alg=none aceito
# tag 1cb4cb
```

## Diferencial desta nota

- **Classic; ainda aparece em libs custom.** Sem isso o playbook da família mente.
- Testo verify path na lib real. Claim admin:true sem verify não é bypass.

Antes de Critical em alg=none, confiro se a telemetria que eu cobraria reagiria — Invalid signature spikes; impossible travel com tokens; denylist.

## Onde já errei

Nem todo JWT 'sem exp' é explorável se houver store server-side.
Não exfiltro tokens de usuários reais — uso contas de teste.

403 no gateway com 200 no origin — path direto e Host conforme ROE.

## Entrega

- blue: Invalid signature spikes; impossible travel com tokens; denylist.
- fix: Bibliotecas atualizadas; enforce algorithm; short TTL + refresh rotation;
bind token a client quando possível; revogação.
- proof: Token de teste manipulado; response privilegiada; libs/versão.

## Refs

- RFC 7519
- PortSwigger JWT
- OWASP JWT Cheat Sheet