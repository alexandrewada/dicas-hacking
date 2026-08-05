---
id: "0046"
categoria: "02-web"
familia: "web-ssrf"
slug: "parser-diff"
angulo: "base"
mitre: ""
owasp: ""
tags: ["02-web", "web-ssrf", "base"]
aliases: ["diferenciais de parser URL", "parser-diff"]
---

# diferenciais de parser URL

## Leitura rápida

SSRF força o servidor a buscar URLs controladas pelo atacante, alcançando rede interna,
metadata cloud (169.254.169.254), e às vezes RCE via gopher/dict em serviços frágeis.
Diferencio SSRF cego vs com resposta, e bypass de allowlists (DNS rebinding,
redirect chains, URL parser differentials, IPv6/decimal IP).

## Foco

- Detalhe que pago pra ver: **Go vs urllib vs browser**.
- Mostro role/creds ou doc interno. Redirect trick só conta se mudar alcance real.

## Mãos na massa

1. Identifico sinks: webhooks, PDF generators, importers, avatars, health checks.
2. Testo http(s) para burp collaborator / interactsh **do engajamento**.
3. Tento metadata endpoints cloud se in-scope.
4. Exploro redirects, DNS rebinding e encodings de IP.
5. Avalio protocolo wrappers apenas se ROE permitir e risco aceito.

## No lab ficou assim

```http
POST /hook/preview HTTP/1.1
Host: app.lab.local
Content-Type: application/json

{"target":"http://internal-admin.lab.local:8080/health"}
# SSRF parser-diff: corpo/timing prova alcance interno — tag 0fd668
```

Impacto que eu aceito: ATO, cross-tenant, escrita privilegiada, RCE. Reflection sem sink útil vira Informational.

## Pitfall

Nem todo fetch é SSRF explorável. WAF pode mascarar.
Não escaneio toda a rede interna sem autorização explícita.

## Detecção / remediação

Egress filtering logs; deny metadata IMDS; alertas para 169.254.169.254.

→ Allowlist de destinos; bloquear link-local; IMDSv2; network policies;
parse URL com lib única e canônica.

## Prova

DNS/HTTP callback proof; (se autorizado) trecho de metadata redigido.

## Refs

- [OWASP SSRF Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html)
- [PortSwigger — SSRF](https://portswigger.net/web-security/ssrf)
- [AWS — IMDSv2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html)

## Relacionadas

- [diferenciais de parser URL — detecção](0426-web-ssrf-parser-diff--detecao.md)
- [diferenciais de parser URL — path](0806-web-ssrf-parser-diff--path.md)
- [SSRF até o IMDS (role cloud)](0041-web-ssrf-imds.md)
- [SSRF cego com out-of-band](0042-web-ssrf-blind.md)
- [SSRF com DNS rebinding](0044-web-ssrf-dns-rebind.md)