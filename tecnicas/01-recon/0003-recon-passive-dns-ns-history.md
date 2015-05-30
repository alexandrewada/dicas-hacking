# histórico de nameservers e risco de hijack

**A05:2021 Security Misconfiguration / A01 Broken Access (superficie)** · `T1590 Gather Victim Network Information`

Em engajamentos autorizados, DNS é frequentemente a primeira fonte de verdade sobre a superfície externa.
Registros A/AAAA, CNAME, MX, TXT (SPF/DKIM/DMARC), NS e histórico (SecurityTrails, VirusTotal, crt.sh)
revelam hosts esquecidos, ambientes de staging e cadeias de CDN.
O objetivo não é 'encontrar tudo no Google', e sim construir um **grafo de ativos** correlacionável com certificados,
ASN e padrões de nomenclatura corporativa.

**Variante:** NS antigos ainda aceitando updates dinâmicos são achado de alto impacto.

**Método**

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
# marcar dev-/staging- ; tag a0e2b0 (ns-history)
```

**Freio:** Wildcard DNS gera falsos positivos massivos.

histórico de nameservers e risco de hijack: se não reproduz efeito (authz/dado/exec), não infla severidade. Referência de sinal: SIEM/DNS logs: picos de consultas a subdomínios inexistentes. Certificate Transparency monitoring (e.

Detecto via: SIEM/DNS logs: picos de consultas a subdomínios inexistentes.
Certificate Transparency monitoring (ex.: certstream) para novos hosts.

Corrijo com: Inventário contínuo de ativos; remover staging exposto; DMARC p=reject;
segmentar DNS interno vs externo; alertas em mudanças de NS/MX.

Levo no report: Lista de FQDN + fonte + timestamp; evidência de certificado; mapa ASN.

Refs: OWASP Testing Guide WSTG-INFO, MITRE ATT&CK T1590, RFC 1035