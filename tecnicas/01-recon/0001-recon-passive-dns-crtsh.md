# via Certificate Transparency (crt.sh)

## Leitura rápida

Em engajamentos autorizados, DNS é frequentemente a primeira fonte de verdade sobre a superfície externa.
Registros A/AAAA, CNAME, MX, TXT (SPF/DKIM/DMARC), NS e histórico (SecurityTrails, VirusTotal, crt.sh)
revelam hosts esquecidos, ambientes de staging e cadeias de CDN.
O objetivo não é 'encontrar tudo no Google', e sim construir um **grafo de ativos** correlacionável com certificados,
ASN e padrões de nomenclatura corporativa.

## Foco

- Foco em deduplicar SANs e detectar padrões `dev-`, `staging-`, `vpn-`.
- **Correlacione data de emissão com janelas de deploy** — muda ruído e o que entra no PDF.
- Deduplico SANs; marco dev-/staging-/vpn-; correlaciono emissão com deploy.

## Mãos na massa

1. Coleto domínio seed autorizado e wildcards do escopo.
2. Extrair SANs de certificados via crt.sh / Censys (somente leitura pública).
3. Resolver passivamente; marcar NXDOMAIN vs wildcards.
4. Agrupar por ASN e CDN; isolar origin IPs quando política permitir.
5. Cruzar com WHOIS histórico e mudanças de NS (hijack residual).
6. Entregar inventário com criticidade e dono presumido.

## No lab ficou assim

```bash
# recon passivo autorizado
curl -sS 'https://crt.sh/?q=%25.lab.local&output=json' | jq '.[].name_value' | sort -u
# marcar dev-/staging- ; tag 152131 (crtsh)
```

CNAME órfão com cache CDN mentindo: confirmo NXDOMAIN/whois do alvo antes de Critical.

## Pitfall

Wildcard DNS gera falsos positivos massivos.
Subdomínios em CDN não implicam origem vulnerável.
Dados públicos podem estar desatualizados — valide no escopo ativo só com autorização.

## Detecção / remediação

SIEM/DNS logs: picos de consultas a subdomínios inexistentes.
Certificate Transparency monitoring (ex.: certstream) para novos hosts.

→ Inventário contínuo de ativos; remover staging exposto; DMARC p=reject;
segmentar DNS interno vs externo; alertas em mudanças de NS/MX.

## Prova

Lista de FQDN + fonte + timestamp; evidência de certificado; mapa ASN.

## Refs

- OWASP Testing Guide WSTG-INFO
- MITRE ATT&CK T1590
- RFC 1035