# CSP como mapa de domínios — path

CSP como mapa de domínios como pivô. Path curto > monte de finding isolado.

## Papel

Headers, ordem de cipher suites, HTTP/2 SETTINGS, cookies default e páginas de erro
permitem identificar stacks (IIS, nginx, Tomcat, Spring, Cloudflare) com baixa intrusão.
Em pentest externo, fingerprint preciso reduz ruído e evita payloads incompatíveis.

## Por que pivota

- Detalhe que pago pra ver: **directives revelam CDNs, analytics e S3 buckets**.

## Cadeia

1. Entrada (escopo)
2. Pivô: CSP como mapa de domínios
3. Objetivo do ROE
4. Persistência só se pedido, com kill-switch

## Execução do pivô

1. Capturo response headers e cookies em request baseline.
2. Observar HTTP/2 e ALPN via TLS handshake autorizado.
3. Comparar com fingerprints conhecidos (wappalyzer logic / ja3s com cuidado).
4. Mapeio painéis admin por path heuristics **sem** força bruta agressiva.
5. Registrar versões expostas (Server, X-Powered-By) como finding informativo.

## No lab ficou assim

```bash
# recon passivo autorizado
curl -sS 'https://crt.sh/?q=%25.lab.local&output=json' | jq '.[].name_value' | sort -u
# marcar dev-/staging- ; tag 1d57ed (csp-leak)
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

CT + DNS history + SANs viram mapa. Scan wide fora do ROE porque o ASN 'parece' do cliente é pedrada.

## Refs

- WSTG-INFO-02
- RFC 9110
- OWASP Secure Headers