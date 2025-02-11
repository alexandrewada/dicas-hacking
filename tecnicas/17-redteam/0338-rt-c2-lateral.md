# lateral com credenciais de engajamento

**Red Team** · `T1071 Application Layer Protocol`

## Contexto

C2 em red team deve priorizar ROE, kill-switch, allowlists de beacon e evitar
impacto em disponibilidade. OpSec inclui metadados de infraestrutura, categorificação de domínios
e alinhamento com detection goals do purple team.

## Como eu faço

1. Definir canais permitidos (HTTPS, DNS, etc.).
2. Infra com segregação e burndown plan.
3. Payloads assinados apenas em alvos autorizados.
4. Telemetria mínima necessária para objetivos.
5. Desmobilizar infra ao final.

## No lab ficou assim

```bash
# C2 lab — kill-switch e janela
curl -sk https://c2.lab.local/lateral/beacon -H 'X-Session: 90dd28'
# só conta teste; sem persistência fora do ROE
```

## Diferencial desta nota

- Variante lateral com credenciais de engajamento: trato separado da família `rt-c2`.

Antes de Critical em lateral com credenciais de engajamento, confiro se a telemetria que eu cobraria reagiria — CDN/proxy anomalies; beacon jitter patterns; JA3.

## Onde já errei

Não uso infra de C2 criminal. Não aponte para fora do escopo.

Timeline + decisões de não-exploração pesam no report.

## Entrega

- blue: CDN/proxy anomalies; beacon jitter patterns; JA3.
- fix: Allowlist egress; TLS inspection onde adequado; DNS control.
- proof: Diagrama de infra; IOCs entregues ao blue; timeline.

## Refs

- Red Team Field Manual ethics
- MITRE C2