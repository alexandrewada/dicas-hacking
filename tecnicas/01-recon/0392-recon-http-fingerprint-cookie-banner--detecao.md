---
id: "0392"
categoria: "01-recon"
familia: "recon-http-fingerprint"
slug: "cookie-banner"
angulo: "detecao"
mitre: "T1592"
owasp: "WSTG-INFO-02"
tags: ["01-recon", "recon-http-fingerprint", "detecao", "t1592"]
aliases: ["cookies default de framework", "cookie-banner", "cookie-banner-detecao"]
---

# cookies default de framework — detecção

Purple em cookies default de framework: uma execução limpa. A pergunta é se alertou — não se o exploit 'passa'.

## Contexto

Headers, ordem de cipher suites, HTTP/2 SETTINGS, cookies default e páginas de erro
permitem identificar stacks (IIS, nginx, Tomcat, Spring, Cloudflare) com baixa intrusão.
Em pentest externo, fingerprint preciso reduz ruído e evita payloads incompatíveis.

## Hipótese

- **JSESSIONID, PHPSESSID, ASP.NET_SessionId como pista de stack.** Sem isso o playbook da família mente.

## Como corro o purple

1. Janela combinada com blue (ou auto-lab).
2. Telemetria mínima no ar.
3. PoC **uma** vez.
4. MTTD + qualidade do playbook.
5. Silêncio → gap + esboço de regra amarrado a `T1592 Gather Victim Host Information`.

### PoC

1. Capturo response headers e cookies em request baseline.
2. Observar HTTP/2 e ALPN via TLS handshake autorizado.
3. Comparar com fingerprints conhecidos (wappalyzer logic / ja3s com cuidado).
4. Mapeio painéis admin por path heuristics **sem** força bruta agressiva.
5. Registrar versões expostas (Server, X-Powered-By) como finding informativo.

## Sinal / query

```text
CT monitor: new SAN *.lab.local issued
DNS NXDOMAIN spike for enum pattern — cookie-banner 275de6
```

## Sinal

Detectar scanners por User-Agent e ritmo de probes.
Alertar exposição de versões em headers.

## Freio

WAF pode randomizar headers. Não confie só em `Server:`.
JA3/JA3S podem colidir; use como sinal, não prova.

Achado de recon que eu reporto: ativo fora do inventário com superfície autenticada, ou takeover com prova de controle — lista crua de subdomínio não conta.

## Evidência

Request/response sanitizados; versão inferida; confiança (alta/média/baixa).

Timestamp + identidade lab + query SIEM — ou declaração explícita de alerta que não veio.

## Refs

- [MITRE ATT&CK T1592](https://attack.mitre.org/techniques/T1592/)
- [WSTG-INFO-02](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/01-Information_Gathering/02-Fingerprint_Web_Server)
- [RFC 9110 — HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110)
- [OWASP Secure Headers Project](https://owasp.org/www-project-secure-headers/)
- [PortSwigger — HTTP information gathering](https://portswigger.net/web-security)

## Relacionadas

- [cookies default de framework](0012-recon-http-fingerprint-cookie-banner.md)
- [cookies default de framework — path](0772-recon-http-fingerprint-cookie-banner--path.md)
- [endpoints ACME/challenge](0020-recon-http-fingerprint-acme-probe.md)
- [heurística via Cache-Control/ETag](0017-recon-http-fingerprint-cache-headers.md)
- [CSP como mapa de domínios](0019-recon-http-fingerprint-csp-leak.md)
- [páginas de erro verbosas](0013-recon-http-fingerprint-error-page.md)