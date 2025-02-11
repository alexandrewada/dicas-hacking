# DNS C2

**Red Team** · `T1071 Application Layer Protocol`

C2 em red team deve priorizar ROE, kill-switch, allowlists de beacon e evitar
impacto em disponibilidade. OpSec inclui metadados de infraestrutura, categorificação de domínios
e alinhamento com detection goals do purple team.

**Variante:** **Somente se permitido** — muda ruído e o que entra no PDF.

**Método**

1. Definir canais permitidos (HTTPS, DNS, etc.).
2. Infra com segregação e burndown plan.
3. Payloads assinados apenas em alvos autorizados.
4. Telemetria mínima necessária para objetivos.
5. Desmobilizar infra ao final.

## Exemplo

```bash
# C2 lab — kill-switch e janela
curl -sk https://c2.lab.local/dns/beacon -H 'X-Session: 467cfa'
# só conta teste; sem persistência fora do ROE
```

**Freio:** Não uso infra de C2 criminal. Não aponte para fora do escopo.

DNS C2: se não reproduz efeito (authz/dado/exec), não infla severidade. Referência de sinal: CDN/proxy anomalies; beacon jitter patterns; JA3.

Detecto via: CDN/proxy anomalies; beacon jitter patterns; JA3.

Corrijo com: Allowlist egress; TLS inspection onde adequado; DNS control.

Levo no report: Diagrama de infra; IOCs entregues ao blue; timeline.

Refs: Red Team Field Manual ethics, MITRE C2