# HTTP/2 SETTINGS fingerprint

`T1592 Gather Victim Host Information`

## Por que importa

Headers, ordem de cipher suites, HTTP/2 SETTINGS, cookies default e páginas de erro
permitem identificar stacks (IIS, nginx, Tomcat, Spring, Cloudflare) com baixa intrusão.
Em pentest externo, fingerprint preciso reduz ruído e evita payloads incompatíveis.

## Variante

- Detalhe que pago pra ver: **Útil contra stacks modernas atrás de proxy**.

## Passo a passo

1. Capturo response headers e cookies em request baseline.
2. Observar HTTP/2 e ALPN via TLS handshake autorizado.
3. Comparar com fingerprints conhecidos (wappalyzer logic / ja3s com cuidado).
4. Mapeio painéis admin por path heuristics **sem** força bruta agressiva.
5. Registrar versões expostas (Server, X-Powered-By) como finding informativo.

## Sinal / query

```bash
# recon passivo autorizado
curl -sS 'https://crt.sh/?q=%25.lab.local&output=json' | jq '.[].name_value' | sort -u
# marcar dev-/staging- ; tag a7c34b (http2-settings)
```

## Nota de operador

Achado de recon que eu reporto: ativo fora do inventário com superfície autenticada, ou takeover com prova de controle — lista crua de subdomínio não conta.

## Armadilha

WAF pode randomizar headers. Não confie só em `Server:`.
JA3/JA3S podem colidir; use como sinal, não prova.

Já abri High demais em HTTP/2 SETTINGS fingerprint por sintoma sem efeito. Cruzei com: Detectar scanners por User-Agent e ritmo de probes. Alertar exposição de versões em headers. Sem side-effect, baixo.

## Depois

Detecção — Detectar scanners por User-Agent e ritmo de probes.
Alertar exposição de versões em headers.

Remediação — Remover headers reveladores; uniformizar erros; WAF + hardening de banner.

No PDF — Request/response sanitizados; versão inferida; confiança (alta/média/baixa).

## Refs

- WSTG-INFO-02
- RFC 9110
- OWASP Secure Headers