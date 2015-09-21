# paths /.well-known/ — detecção

Se o SOC não vê paths /.well-known/, o finding é de cobertura, não de ego ofensivo.

## Contexto

Headers, ordem de cipher suites, HTTP/2 SETTINGS, cookies default e páginas de erro
permitem identificar stacks (IIS, nginx, Tomcat, Spring, Cloudflare) com baixa intrusão.
Em pentest externo, fingerprint preciso reduz ruído e evita payloads incompatíveis.

## Hipótese

- Se não validar **security.txt, change-password, oauth-authorization-server**, a nota fica genérica.

## Como corro o purple

Combinar canal → executar → medir. Sem desligar controle pra 'passar'.

### PoC

1. Capturo response headers e cookies em request baseline.
2. Observar HTTP/2 e ALPN via TLS handshake autorizado.
3. Comparar com fingerprints conhecidos (wappalyzer logic / ja3s com cuidado).
4. Mapeio painéis admin por path heuristics **sem** força bruta agressiva.
5. Registrar versões expostas (Server, X-Powered-By) como finding informativo.

## Sinal / query

```text
CT monitor: new SAN *.lab.local issued
DNS NXDOMAIN spike for enum pattern — well-known ace3e2
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

- WSTG-INFO-02
- RFC 9110
- OWASP Secure Headers