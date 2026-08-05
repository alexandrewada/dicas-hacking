---
id: "0429"
categoria: "02-web"
familia: "web-ssrf"
slug: "webhook"
angulo: "detecao"
mitre: "T1090"
owasp: ""
tags: ["02-web", "web-ssrf", "detecao", "t1090"]
aliases: ["webhooks de CI/CD", "webhook", "webhook-detecao"]
---

# webhooks de CI/CD — detecção

Purple em webhooks de CI/CD: uma execução limpa. A pergunta é se alertou — não se o exploit 'passa'.

## Contexto

SSRF força o servidor a buscar URLs controladas pelo atacante, alcançando rede interna,
metadata cloud (169.254.169.254), e às vezes RCE via gopher/dict em serviços frágeis.
Diferencio SSRF cego vs com resposta, e bypass de allowlists (DNS rebinding,
redirect chains, URL parser differentials, IPv6/decimal IP).

## Hipótese

- **Impacto em supply chain interno.** Sem isso o playbook da família mente.
- Mostro role/creds ou doc interno. Redirect trick só conta se mudar alcance real.

## Como corro o purple

1. Janela combinada com blue (ou auto-lab).
2. Telemetria mínima no ar.
3. PoC **uma** vez.
4. MTTD + qualidade do playbook.
5. Silêncio → gap + esboço de regra amarrado a `T1090 Proxy / T1552 Unsecured Credentials (metadata)`.

### PoC

1. Identifico sinks: webhooks, PDF generators, importers, avatars, health checks.
2. Testo http(s) para burp collaborator / interactsh **do engajamento**.
3. Tento metadata endpoints cloud se in-scope.
4. Exploro redirects, DNS rebinding e encodings de IP.
5. Avalio protocolo wrappers apenas se ROE permitir e risco aceito.

## Sinal / query

```text
egress_proxy deny link-local + RFC1918 não allowlisted
log: src=app dst=internal-admin.lab.local action=ALLOW? → gap (webhook/56a3f2)
```

## Sinal

Egress filtering logs; deny metadata IMDS; alertas para 169.254.169.254.

## Freio

Nem todo fetch é SSRF explorável. WAF pode mascarar.
Não escaneio toda a rede interna sem autorização explícita.

WAF bypass só depois da prova de impacto. Senão vira discussão de tool com o blue.

## Evidência

DNS/HTTP callback proof; (se autorizado) trecho de metadata redigido.

Timestamp + identidade lab + query SIEM — ou declaração explícita de alerta que não veio.

## Refs

- [MITRE ATT&CK T1090](https://attack.mitre.org/techniques/T1090/)
- [MITRE ATT&CK T1552](https://attack.mitre.org/techniques/T1552/)
- [OWASP SSRF Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html)
- [PortSwigger — SSRF](https://portswigger.net/web-security/ssrf)
- [AWS — IMDSv2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html)

## Relacionadas

- [webhooks de CI/CD](0049-web-ssrf-webhook.md)
- [webhooks de CI/CD — path](0809-web-ssrf-webhook--path.md)
- [SSRF até o IMDS (role cloud)](0041-web-ssrf-imds.md)
- [SSRF cego com out-of-band](0042-web-ssrf-blind.md)
- [SSRF com DNS rebinding](0044-web-ssrf-dns-rebind.md)