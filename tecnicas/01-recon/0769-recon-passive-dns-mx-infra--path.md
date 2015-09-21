# infraestrutura de e-mail e relays — path

infraestrutura de e-mail e relays como pivô. Path curto > monte de finding isolado.

## Papel

Em engajamentos autorizados, DNS é frequentemente a primeira fonte de verdade sobre a superfície externa.
Registros A/AAAA, CNAME, MX, TXT (SPF/DKIM/DMARC), NS e histórico (SecurityTrails, VirusTotal, crt.sh)
revelam hosts esquecidos, ambientes de staging e cadeias de CDN.
O objetivo não é 'encontrar tudo no Google', e sim construir um **grafo de ativos** correlacionável com certificados,
ASN e padrões de nomenclatura corporativa.

## Por que pivota

- **Relays abertos e gateways legados ampliam phishing interno** — muda ruído e o que entra no PDF.

## Cadeia

1. Entrada (escopo)
2. Pivô: infraestrutura de e-mail e relays
3. Objetivo do ROE
4. Persistência só se pedido, com kill-switch

## Execução do pivô

1. Coleto domínio seed autorizado e wildcards do escopo.
2. Extrair SANs de certificados via crt.sh / Censys (somente leitura pública).
3. Resolver passivamente; marcar NXDOMAIN vs wildcards.
4. Agrupar por ASN e CDN; isolar origin IPs quando política permitir.
5. Cruzar com WHOIS histórico e mudanças de NS (hijack residual).
6. Entregar inventário com criticidade e dono presumido.

## No lab ficou assim

```bash
# relay lab — segmento acordado, conta teste
ntlmrelayx.py -t smb://TARGET.lab.local -smb2support --no-dump
# trigger mx-infra; evidência: auth USER_A + ação não destrutiva tag dba9dd
```

## Freio

Wildcard DNS gera falsos positivos massivos.
Subdomínios em CDN não implicam origem vulnerável.
Dados públicos podem estar desatualizados — valide no escopo ativo só com autorização.

## No caminho

Detectar: SIEM/DNS logs: picos de consultas a subdomínios inexistentes.
Certificate Transparency monitoring (ex.: certstream) para novos hosts.

Remediar: Inventário contínuo de ativos; remover staging exposto; DMARC p=reject;
segmentar DNS interno vs externo; alertas em mudanças de NS/MX.

## Prova

Lista de FQDN + fonte + timestamp; evidência de certificado; mapa ASN.

CNAME órfão com cache CDN mentindo: confirmo NXDOMAIN/whois do alvo antes de Critical.

## Refs

- OWASP Testing Guide WSTG-INFO
- MITRE ATT&CK T1590
- RFC 1035