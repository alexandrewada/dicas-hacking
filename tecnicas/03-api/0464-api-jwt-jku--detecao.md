# jku/x5u SSRF + key inject — detecção

Purple em jku/x5u SSRF + key inject: uma execução limpa. A pergunta é se alertou — não se o exploit 'passa'.

## Contexto

JWTs mal implementados permitem alg=none, confusão RS256/HS256, kid injection (SQL/path),
claims sensíveis sem validação de iss/aud/exp, e tokens eternamente válidos sem revogação.
Valido a biblioteca verificadora, não só o conteúdo do token.

## Hipótese

- Detalhe que pago pra ver: **Hospede JWKS só se ROE permitir**.
- Mostro role/creds ou doc interno. Redirect trick só conta se mudar alcance real.
- Testo verify path na lib real. Claim admin:true sem verify não é bypass.

## Como corro o purple

1. Janela combinada com blue (ou auto-lab).
2. Telemetria mínima no ar.
3. PoC **uma** vez.
4. MTTD + qualidade do playbook.
5. Silêncio → gap + esboço de regra amarrado a `T1550 Use Alternate Authentication Material`.

### PoC

1. Decodifico header/payload; mapeio claims.
2. Testo alg none e troca de algoritmo conforme biblioteca.
3. Avalio kid/jku/x5u se presentes (SSRF/file).
4. Verifico aud/iss/nbf/exp e clock skew.
5. Testo privilege claims e token sidejacking.

## Exemplo

```text
authz_fail OR jwt_verify_error claim=jku
alerta se alg in (none, HS256) com key pública — tag c78c04
```

## Sinal

Invalid signature spikes; impossible travel com tokens; denylist.

## Freio

Nem todo JWT 'sem exp' é explorável se houver store server-side.
Não exfiltro tokens de usuários reais — uso contas de teste.

Batch e webhook: ACL costuma autorizar o primeiro ID do array e ignorar o resto. Testo isso cedo.

## Evidência

Token de teste manipulado; response privilegiada; libs/versão.

Timestamp + identidade lab + query SIEM — ou declaração explícita de alerta que não veio.

## Refs

- RFC 7519
- PortSwigger JWT
- OWASP JWT Cheat Sheet