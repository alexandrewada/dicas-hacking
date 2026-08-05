---
id: "0776"
categoria: "01-recon"
familia: "recon-http-fingerprint"
slug: "well-known"
angulo: "path"
mitre: ""
owasp: "WSTG-INFO-02"
tags: ["01-recon", "recon-http-fingerprint", "path"]
aliases: ["paths /.well-known/", "well-known", "well-known-path"]
---

# paths /.well-known/ — path

paths /.well-known/ como pivô. Path curto > monte de finding isolado.

## Papel

Headers, ordem de cipher suites, HTTP/2 SETTINGS, cookies default e páginas de erro
permitem identificar stacks (IIS, nginx, Tomcat, Spring, Cloudflare) com baixa intrusão.
Em pentest externo, fingerprint preciso reduz ruído e evita payloads incompatíveis.

## Por que pivota

- Se não validar **security.txt, change-password, oauth-authorization-server**, a nota fica genérica.

## Cadeia

1. Entrada (escopo)
2. Pivô: paths /.well-known/
3. Objetivo do ROE
4. Persistência só se pedido, com kill-switch

## Execução do pivô

1. Capturo response headers e cookies em request baseline.
2. Observar HTTP/2 e ALPN via TLS handshake autorizado.
3. Comparar com fingerprints conhecidos (wappalyzer logic / ja3s com cuidado).
4. Mapeio painéis admin por path heuristics **sem** força bruta agressiva.
5. Registrar versões expostas (Server, X-Powered-By) como finding informativo.

## Sinal / query

```bash
# recon passivo autorizado
curl -sS 'https://crt.sh/?q=%25.lab.local&output=json' | jq '.[].name_value' | sort -u
# marcar dev-/staging- ; tag 67f10d (well-known)
```

## Freio

WAF pode randomizar headers. Não confie só em `Server:`.
JA3/JA3S podem colidir; use como sinal, não prova.

## No caminho

Detectar: Detectar scanners por User-Agent e ritmo de probes.
Alertar exposição de versões em headers.

Remediar: Remover headers reveladores; uniformizar erros; WAF + hardening de banner.

## Prova

Request/response sanitizados; versão inferida; confiança (alta/média/baixa).

Achado de recon que eu reporto: ativo fora do inventário com superfície autenticada, ou takeover com prova de controle — lista crua de subdomínio não conta.

## Refs

- [WSTG-INFO-02](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/01-Information_Gathering/02-Fingerprint_Web_Server)
- [RFC 9110 — HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110)
- [OWASP Secure Headers Project](https://owasp.org/www-project-secure-headers/)
- [PortSwigger — HTTP information gathering](https://portswigger.net/web-security)

## Relacionadas

- [paths /.well-known/](0016-recon-http-fingerprint-well-known.md)
- [paths /.well-known/ — detecção](0396-recon-http-fingerprint-well-known--detecao.md)
- [endpoints ACME/challenge](0020-recon-http-fingerprint-acme-probe.md)
- [heurística via Cache-Control/ETag](0017-recon-http-fingerprint-cache-headers.md)
- [cookies default de framework](0012-recon-http-fingerprint-cookie-banner.md)
- [CSP como mapa de domínios](0019-recon-http-fingerprint-csp-leak.md)