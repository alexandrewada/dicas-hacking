# falta de validação aud/iss — detecção

Gap de detecção em `T1550 Use Alternate Authentication Material` / falta de validação aud/iss. PoC mínimo, telemetria ligada.

## Contexto

JWTs mal implementados permitem alg=none, confusão RS256/HS256, kid injection (SQL/path),
claims sensíveis sem validação de iss/aud/exp, e tokens eternamente válidos sem revogação.
Valido a biblioteca verificadora, não só o conteúdo do token.

## Hipótese

- Detalhe que pago pra ver: **Token de outro ambiente aceito**.
- Testo verify path na lib real. Claim admin:true sem verify não é bypass.

## Como corro o purple

1. Confirmo log source relevante.
2. Disparo o fluxo abaixo.
3. Anoto alerta / ausência.
4. Se silêncio, abro finding de detecção.

### PoC

1. Decodifico header/payload; mapeio claims.
2. Testo alg none e troca de algoritmo conforme biblioteca.
3. Avalio kid/jku/x5u se presentes (SSRF/file).
4. Verifico aud/iss/nbf/exp e clock skew.
5. Testo privilege claims e token sidejacking.

## Exemplo

```text
authz_fail OR jwt_verify_error claim=aud-iss
alerta se alg in (none, HS256) com key pública — tag 27deb0
```

## Sinal

Invalid signature spikes; impossible travel com tokens; denylist.

## Freio

Nem todo JWT 'sem exp' é explorável se houver store server-side.
Não exfiltro tokens de usuários reais — uso contas de teste.

403 no gateway com 200 no origin — path direto e Host conforme ROE.

## Evidência

Token de teste manipulado; response privilegiada; libs/versão.

Timestamp + identidade lab + query SIEM — ou declaração explícita de alerta que não veio.

## Refs

- RFC 7519
- PortSwigger JWT
- OWASP JWT Cheat Sheet