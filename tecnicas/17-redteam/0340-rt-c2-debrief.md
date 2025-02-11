# debrief com SOC

**Red Team** · `T1071 Application Layer Protocol`

## Contexto

C2 em red team deve priorizar ROE, kill-switch, allowlists de beacon e evitar
impacto em disponibilidade. OpSec inclui metadados de infraestrutura, categorificação de domínios
e alinhamento com detection goals do purple team.

## O que muda aqui

- **Lições learned** — muda ruído e o que entra no PDF.

## Como testo

1. Definir canais permitidos (HTTPS, DNS, etc.).
2. Infra com segregação e burndown plan.
3. Payloads assinados apenas em alvos autorizados.
4. Telemetria mínima necessária para objetivos.
5. Desmobilizar infra ao final.

## No lab ficou assim

```bash
# C2 lab — kill-switch e janela
curl -sk https://c2.lab.local/debrief/beacon -H 'X-Session: 884549'
# só conta teste; sem persistência fora do ROE
```

## Campo

Timeline + decisões de não-exploração pesam no report.

debrief com SOC: se não reproduz efeito (authz/dado/exec), não infla severidade. Referência de sinal: CDN/proxy anomalies; beacon jitter patterns; JA3.

## Já me queimei

Não uso infra de C2 criminal. Não aponte para fora do escopo.

## Blue

- Detectar: CDN/proxy anomalies; beacon jitter patterns; JA3.
- Fechar: Allowlist egress; TLS inspection onde adequado; DNS control.

## Evidência

Diagrama de infra; IOCs entregues ao blue; timeline.

## Refs

- Red Team Field Manual ethics
- MITRE C2