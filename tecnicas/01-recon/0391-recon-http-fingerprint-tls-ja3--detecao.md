---
id: "0391"
categoria: "01-recon"
familia: "recon-http-fingerprint"
slug: "tls-ja3"
angulo: "detecao"
mitre: ""
owasp: "WSTG-INFO-02"
tags: ["01-recon", "recon-http-fingerprint", "detecao"]
aliases: ["perfil TLS/JA3S", "tls-ja3", "tls-ja3-detecao"]
---

# perfil TLS/JA3S — detecção

Se o SOC não vê perfil TLS/JA3S, o finding é de cobertura, não de ego ofensivo.

## Contexto

Headers, ordem de cipher suites, HTTP/2 SETTINGS, cookies default e páginas de erro
permitem identificar stacks (IIS, nginx, Tomcat, Spring, Cloudflare) com baixa intrusão.
Em pentest externo, fingerprint preciso reduz ruído e evita payloads incompatíveis.

## Hipótese

- **Documento cipher suites e ALPN sem downgrade ativo fora do escopo.** Sem isso o playbook da família mente.

## Como corro o purple

Combinar canal → executar → medir. Sem desligar controle pra 'passar'.

### PoC

1. Capturo response headers e cookies em request baseline.
2. Observar HTTP/2 e ALPN via TLS handshake autorizado.
3. Comparar com fingerprints conhecidos (wappalyzer logic / ja3s com cuidado).
4. Mapeio painéis admin por path heuristics **sem** força bruta agressiva.
5. Registrar versões expostas (Server, X-Powered-By) como finding informativo.

## Exemplo

```text
CT monitor: new SAN *.lab.local issued
DNS NXDOMAIN spike for enum pattern — tls-ja3 752425
```

## Sinal

Detectar scanners por User-Agent e ritmo de probes.
Alertar exposição de versões em headers.

## Freio

WAF pode randomizar headers. Não confie só em `Server:`.
JA3/JA3S podem colidir; use como sinal, não prova.

CNAME órfão com cache CDN mentindo: confirmo NXDOMAIN/whois do alvo antes de Critical.

## Evidência

Request/response sanitizados; versão inferida; confiança (alta/média/baixa).

Timestamp + identidade lab + query SIEM — ou declaração explícita de alerta que não veio.

## Refs

- [WSTG-INFO-02](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/01-Information_Gathering/02-Fingerprint_Web_Server)
- [RFC 9110 — HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110)
- [OWASP Secure Headers Project](https://owasp.org/www-project-secure-headers/)
- [PortSwigger — HTTP information gathering](https://portswigger.net/web-security)

## Relacionadas

- [perfil TLS/JA3S](0011-recon-http-fingerprint-tls-ja3.md)
- [perfil TLS/JA3S — path](0771-recon-http-fingerprint-tls-ja3--path.md)
- [endpoints ACME/challenge](0020-recon-http-fingerprint-acme-probe.md)
- [heurística via Cache-Control/ETag](0017-recon-http-fingerprint-cache-headers.md)
- [cookies default de framework](0012-recon-http-fingerprint-cookie-banner.md)
- [CSP como mapa de domínios](0019-recon-http-fingerprint-csp-leak.md)