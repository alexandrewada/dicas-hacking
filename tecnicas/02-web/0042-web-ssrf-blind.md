# SSRF cego com out-of-band

**A10:2021 SSRF** · `T1090 Proxy / T1552 Unsecured Credentials (metadata)`

## Contexto

SSRF força o servidor a buscar URLs controladas pelo atacante, alcançando rede interna,
metadata cloud (169.254.169.254), e às vezes RCE via gopher/dict em serviços frágeis.
Diferencio SSRF cego vs com resposta, e bypass de allowlists (DNS rebinding,
redirect chains, URL parser differentials, IPv6/decimal IP).

## O que muda aqui

- Detalhe que pago pra ver: **Time delays e DNS callbacks**.
- Mostro role/creds ou doc interno. Redirect trick só conta se mudar alcance real.

## Como testo

1. Identifico sinks: webhooks, PDF generators, importers, avatars, health checks.
2. Testo http(s) para burp collaborator / interactsh **do engajamento**.
3. Tento metadata endpoints cloud se in-scope.
4. Exploro redirects, DNS rebinding e encodings de IP.
5. Avalio protocolo wrappers apenas se ROE permitir e risco aceito.

## Exemplo

```http
POST /hook/preview HTTP/1.1
Host: app.lab.local
Content-Type: application/json

{"target":"http://internal-admin.lab.local:8080/health"}
# SSRF blind: corpo/timing prova alcance interno — tag 83c292
```

## Campo

WAF bypass só depois da prova de impacto. Senão vira discussão de tool com o blue.

Falso amigo em SSRF cego com out-of-band: UI/log gritam, impacto não. Exijo Egress filtering logs.

## Já me queimei

Nem todo fetch é SSRF explorável. WAF pode mascarar.
Não escaneio toda a rede interna sem autorização explícita.

## Blue

- Detectar: Egress filtering logs; deny metadata IMDS; alertas para 169.254.169.254.
- Fechar: Allowlist de destinos; bloquear link-local; IMDSv2; network policies;
parse URL com lib única e canônica.

## Evidência

DNS/HTTP callback proof; (se autorizado) trecho de metadata redigido.

## Refs

- OWASP SSRF
- PortSwigger SSRF
- AWS IMDSv2