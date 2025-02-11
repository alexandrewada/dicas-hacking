# Kill-switch de C2

`T1071 Application Layer Protocol`

## Por que importa

C2 em red team deve priorizar ROE, kill-switch, allowlists de beacon e evitar
impacto em disponibilidade. OpSec inclui metadados de infraestrutura, categorificação de domínios
e alinhamento com detection goals do purple team.

## Variante

- Variante kill-switch obrigatório: trato separado da família `rt-c2`.

## Passo a passo

1. Definir canais permitidos (HTTPS, DNS, etc.).
2. Infra com segregação e burndown plan.
3. Payloads assinados apenas em alvos autorizados.
4. Telemetria mínima necessária para objetivos.
5. Desmobilizar infra ao final.

## Exemplo

```bash
# C2 lab — kill-switch e janela
curl -sk https://c2.lab.local/killswitch/beacon -H 'X-Session: fb752b'
# só conta teste; sem persistência fora do ROE
```

## Nota de operador

Timeline + decisões de não-exploração pesam no report.

## Armadilha

Não uso infra de C2 criminal. Não aponte para fora do escopo.

Já abri High demais em kill-switch obrigatório por sintoma sem efeito. Cruzei com: CDN/proxy anomalies; beacon jitter patterns; JA3. Sem side-effect, baixo.

## Depois

Detecção — CDN/proxy anomalies; beacon jitter patterns; JA3.

Remediação — Allowlist egress; TLS inspection onde adequado; DNS control.

No PDF — Diagrama de infra; IOCs entregues ao blue; timeline.

## Refs

- Red Team Field Manual ethics
- MITRE C2