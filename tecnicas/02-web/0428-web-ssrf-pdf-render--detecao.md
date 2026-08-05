---
id: "0428"
categoria: "02-web"
familia: "web-ssrf"
slug: "pdf-render"
angulo: "detecao"
mitre: ""
owasp: ""
tags: ["02-web", "web-ssrf", "detecao"]
aliases: ["SSRF via HTML-to-PDF", "pdf-render", "pdf-render-detecao"]
---

# SSRF via HTML-to-PDF — detecção

Se o SOC não vê SSRF via HTML-to-PDF, o finding é de cobertura, não de ego ofensivo.

## Contexto

SSRF força o servidor a buscar URLs controladas pelo atacante, alcançando rede interna,
metadata cloud (169.254.169.254), e às vezes RCE via gopher/dict em serviços frágeis.
Diferencio SSRF cego vs com resposta, e bypass de allowlists (DNS rebinding,
redirect chains, URL parser differentials, IPv6/decimal IP).

## Hipótese

- Detalhe que pago pra ver: **Classic em geradores de invoice**.
- Mostro role/creds ou doc interno. Redirect trick só conta se mudar alcance real.

## Como corro o purple

Combinar canal → executar → medir. Sem desligar controle pra 'passar'.

### PoC

1. Identifico sinks: webhooks, PDF generators, importers, avatars, health checks.
2. Testo http(s) para burp collaborator / interactsh **do engajamento**.
3. Tento metadata endpoints cloud se in-scope.
4. Exploro redirects, DNS rebinding e encodings de IP.
5. Avalio protocolo wrappers apenas se ROE permitir e risco aceito.

## Exemplo

```text
egress_proxy deny link-local + RFC1918 não allowlisted
log: src=app dst=internal-admin.lab.local action=ALLOW? → gap (pdf-render/8f1c52)
```

## Sinal

Egress filtering logs; deny metadata IMDS; alertas para 169.254.169.254.

## Freio

Nem todo fetch é SSRF explorável. WAF pode mascarar.
Não escaneio toda a rede interna sem autorização explícita.

Impacto que eu aceito: ATO, cross-tenant, escrita privilegiada, RCE. Reflection sem sink útil vira Informational.

## Evidência

DNS/HTTP callback proof; (se autorizado) trecho de metadata redigido.

Timestamp + identidade lab + query SIEM — ou declaração explícita de alerta que não veio.

## Refs

- [OWASP SSRF Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html)
- [PortSwigger — SSRF](https://portswigger.net/web-security/ssrf)
- [AWS — IMDSv2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html)

## Relacionadas

- [SSRF via HTML-to-PDF](0048-web-ssrf-pdf-render.md)
- [SSRF via HTML-to-PDF — path](0808-web-ssrf-pdf-render--path.md)
- [SSRF até o IMDS (role cloud)](0041-web-ssrf-imds.md)
- [SSRF cego com out-of-band](0042-web-ssrf-blind.md)
- [SSRF com DNS rebinding](0044-web-ssrf-dns-rebind.md)