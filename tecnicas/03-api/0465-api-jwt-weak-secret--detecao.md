---
id: "0465"
categoria: "03-api"
familia: "api-jwt"
slug: "weak-secret"
angulo: "detecao"
mitre: "T1550"
owasp: ""
tags: ["03-api", "api-jwt", "detecao", "t1550"]
aliases: ["HMAC secret fraco", "weak-secret", "weak-secret-detecao"]
---

# HMAC secret fraco — detecção

Se o SOC não vê HMAC secret fraco, o finding é de cobertura, não de ego ofensivo.

## Contexto

JWTs mal implementados permitem alg=none, confusão RS256/HS256, kid injection (SQL/path),
claims sensíveis sem validação de iss/aud/exp, e tokens eternamente válidos sem revogação.
Valido a biblioteca verificadora, não só o conteúdo do token.

## Hipótese

- **Crack offline com wordlist autorizada.** Sem isso o playbook da família mente.
- Testo verify path na lib real. Claim admin:true sem verify não é bypass.

## Como corro o purple

Combinar canal → executar → medir. Sem desligar controle pra 'passar'.

### PoC

1. Decodifico header/payload; mapeio claims.
2. Testo alg none e troca de algoritmo conforme biblioteca.
3. Avalio kid/jku/x5u se presentes (SSRF/file).
4. Verifico aud/iss/nbf/exp e clock skew.
5. Testo privilege claims e token sidejacking.

## Sinal / query

```text
authz_fail OR jwt_verify_error claim=weak-secret
alerta se alg in (none, HS256) com key pública — tag 150f7d
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

- [MITRE ATT&CK T1550](https://attack.mitre.org/techniques/T1550/)
- [RFC 7519 — JWT](https://www.rfc-editor.org/rfc/rfc7519)
- [PortSwigger — JWT attacks](https://portswigger.net/web-security/jwt)
- [OWASP JWT Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/JSON_Web_Token_Cheat_Sheet.html)

## Relacionadas

- [HMAC secret fraco](0085-api-jwt-weak-secret.md)
- [HMAC secret fraco — path](0845-api-jwt-weak-secret--path.md)
- [JWT com alg=none](0081-api-jwt-alg-none.md)
- [Confusão RS256/HS256](0082-api-jwt-rs-hs.md)
- [tampering de role/admin](0086-api-jwt-claim-tamper.md)