# SSRF com DNS rebinding — detecção

Se o SOC não vê SSRF com DNS rebinding, o finding é de cobertura, não de ego ofensivo.

## Contexto

SSRF força o servidor a buscar URLs controladas pelo atacante, alcançando rede interna,
metadata cloud (169.254.169.254), e às vezes RCE via gopher/dict em serviços frágeis.
Diferencio SSRF cego vs com resposta, e bypass de allowlists (DNS rebinding,
redirect chains, URL parser differentials, IPv6/decimal IP).

## Hipótese

- **TTL baixo para burlar checagem toctou** — muda ruído e o que entra no PDF.
- Mostro role/creds ou doc interno. Redirect trick só conta se mudar alcance real.

## Como corro o purple

Combinar canal → executar → medir. Sem desligar controle pra 'passar'.

### PoC

1. Identifico sinks: webhooks, PDF generators, importers, avatars, health checks.
2. Testo http(s) para burp collaborator / interactsh **do engajamento**.
3. Tento metadata endpoints cloud se in-scope.
4. Exploro redirects, DNS rebinding e encodings de IP.
5. Avalio protocolo wrappers apenas se ROE permitir e risco aceito.

## Sinal / query

```text
egress_proxy deny link-local + RFC1918 não allowlisted
log: src=app dst=internal-admin.lab.local action=ALLOW? → gap (dns-rebind/080674)
```

## Sinal

Egress filtering logs; deny metadata IMDS; alertas para 169.254.169.254.

## Freio

Nem todo fetch é SSRF explorável. WAF pode mascarar.
Não escaneio toda a rede interna sem autorização explícita.

Parâmetro é boundary: de onde veio o valor (cookie, claim, hidden) importa mais que o payload da vez.

## Evidência

DNS/HTTP callback proof; (se autorizado) trecho de metadata redigido.

Timestamp + identidade lab + query SIEM — ou declaração explícita de alerta que não veio.

## Refs

- OWASP SSRF
- PortSwigger SSRF
- AWS IMDSv2