# domain fronting histórico

**Red Team** · `T1071 Application Layer Protocol`

## Contexto

C2 em red team deve priorizar ROE, kill-switch, allowlists de beacon e evitar
impacto em disponibilidade. OpSec inclui metadados de infraestrutura, categorificação de domínios
e alinhamento com detection goals do purple team.

## O que muda aqui

- **Status atual/limites.** Sem isso o playbook da família mente.

## Como testo

1. Definir canais permitidos (HTTPS, DNS, etc.).
2. Infra com segregação e burndown plan.
3. Payloads assinados apenas em alvos autorizados.
4. Telemetria mínima necessária para objetivos.
5. Desmobilizar infra ao final.

## PoC mínimo

```bash
# C2 lab — kill-switch e janela
curl -sk https://c2.lab.local/domain-front/beacon -H 'X-Session: 8a0e6f'
# só conta teste; sem persistência fora do ROE
```

## Campo

C2/persistência com kill-switch e janela. Beacon sem objetivo é ego.

Falso amigo em domain fronting histórico: UI/log gritam, impacto não. Exijo CDN/proxy anomalies.

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