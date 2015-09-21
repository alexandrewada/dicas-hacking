# análise SPF/DKIM para takeover de envio — detecção

Purple em análise SPF/DKIM para takeover de envio: uma execução limpa. A pergunta é se alertou — não se o exploit 'passa'.

## Contexto

Em engajamentos autorizados, DNS é frequentemente a primeira fonte de verdade sobre a superfície externa.
Registros A/AAAA, CNAME, MX, TXT (SPF/DKIM/DMARC), NS e histórico (SecurityTrails, VirusTotal, crt.sh)
revelam hosts esquecidos, ambientes de staging e cadeias de CDN.
O objetivo não é 'encontrar tudo no Google', e sim construir um **grafo de ativos** correlacionável com certificados,
ASN e padrões de nomenclatura corporativa.

## Hipótese

- **Mecanismos `include:` órfãos e IP4 removidos criam risco de spoofing** — muda ruído e o que entra no PDF.
- **Valide com checkdmarc; proponha hardening no relatório** — muda ruído e o que entra no PDF.
- include órfão = spoof. checkdmarc + proposta (-all / reject).

## Como corro o purple

1. Janela combinada com blue (ou auto-lab).
2. Telemetria mínima no ar.
3. PoC **uma** vez.
4. MTTD + qualidade do playbook.
5. Silêncio → gap + esboço de regra amarrado a `T1590 Gather Victim Network Information`.

### PoC

1. Coleto domínio seed autorizado e wildcards do escopo.
2. Extrair SANs de certificados via crt.sh / Censys (somente leitura pública).
3. Resolver passivamente; marcar NXDOMAIN vs wildcards.
4. Agrupar por ASN e CDN; isolar origin IPs quando política permitir.
5. Cruzar com WHOIS histórico e mudanças de NS (hijack residual).
6. Entregar inventário com criticidade e dono presumido.

## Sinal / query

```text
CT monitor: new SAN *.lab.local issued
DNS NXDOMAIN spike for enum pattern — spf-takeover 5e4f5d
```

## Sinal

SIEM/DNS logs: picos de consultas a subdomínios inexistentes.
Certificate Transparency monitoring (ex.: certstream) para novos hosts.

## Freio

Wildcard DNS gera falsos positivos massivos.
Subdomínios em CDN não implicam origem vulnerável.
Dados públicos podem estar desatualizados — valide no escopo ativo só com autorização.

CT + DNS history + SANs viram mapa. Scan wide fora do ROE porque o ASN 'parece' do cliente é pedrada.

## Evidência

Lista de FQDN + fonte + timestamp; evidência de certificado; mapa ASN.

Timestamp + identidade lab + query SIEM — ou declaração explícita de alerta que não veio.

## Refs

- OWASP Testing Guide WSTG-INFO
- MITRE ATT&CK T1590
- RFC 1035