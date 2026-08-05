---
id: "0802"
categoria: "02-web"
familia: "web-ssrf"
slug: "blind"
angulo: "path"
mitre: "T1090"
owasp: ""
tags: ["02-web", "web-ssrf", "path", "t1090"]
aliases: ["SSRF cego com out-of-band", "blind", "blind-path"]
---

# SSRF cego com out-of-band — path

SSRF cego com out-of-band como pivô. Path curto > monte de finding isolado.

## Papel

SSRF força o servidor a buscar URLs controladas pelo atacante, alcançando rede interna,
metadata cloud (169.254.169.254), e às vezes RCE via gopher/dict em serviços frágeis.
Diferencio SSRF cego vs com resposta, e bypass de allowlists (DNS rebinding,
redirect chains, URL parser differentials, IPv6/decimal IP).

## Por que pivota

- Detalhe que pago pra ver: **Time delays e DNS callbacks**.
- Mostro role/creds ou doc interno. Redirect trick só conta se mudar alcance real.

## Cadeia

1. Entrada (escopo)
2. Pivô: SSRF cego com out-of-band
3. Objetivo do ROE
4. Persistência só se pedido, com kill-switch

## Execução do pivô

1. Identifico sinks: webhooks, PDF generators, importers, avatars, health checks.
2. Testo http(s) para burp collaborator / interactsh **do engajamento**.
3. Tento metadata endpoints cloud se in-scope.
4. Exploro redirects, DNS rebinding e encodings de IP.
5. Avalio protocolo wrappers apenas se ROE permitir e risco aceito.

## Sinal / query

```http
POST /hook/preview HTTP/1.1
Host: app.lab.local
Content-Type: application/json

{"target":"http://internal-admin.lab.local:8080/health"}
# SSRF blind: corpo/timing prova alcance interno — tag 2b91f7
```

## Freio

Nem todo fetch é SSRF explorável. WAF pode mascarar.
Não escaneio toda a rede interna sem autorização explícita.

## No caminho

Detectar: Egress filtering logs; deny metadata IMDS; alertas para 169.254.169.254.

Remediar: Allowlist de destinos; bloquear link-local; IMDSv2; network policies;
parse URL com lib única e canônica.

## Prova

DNS/HTTP callback proof; (se autorizado) trecho de metadata redigido.

WAF bypass só depois da prova de impacto. Senão vira discussão de tool com o blue.

## Refs

- [MITRE ATT&CK T1090](https://attack.mitre.org/techniques/T1090/)
- [MITRE ATT&CK T1552](https://attack.mitre.org/techniques/T1552/)
- [OWASP SSRF Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html)
- [PortSwigger — SSRF](https://portswigger.net/web-security/ssrf)
- [AWS — IMDSv2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html)

## Relacionadas

- [SSRF cego com out-of-band](0042-web-ssrf-blind.md)
- [SSRF cego com out-of-band — detecção](0422-web-ssrf-blind--detecao.md)
- [SSRF até o IMDS (role cloud)](0041-web-ssrf-imds.md)
- [SSRF com DNS rebinding](0044-web-ssrf-dns-rebind.md)
- [XXE → SSRF (path)](../07-ssrf-xxe/0172-xxe-classic-ssrf.md)