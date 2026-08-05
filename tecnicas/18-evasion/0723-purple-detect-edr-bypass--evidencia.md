---
id: "0723"
categoria: "18-evasion"
familia: "purple-detect"
slug: "edr-bypass"
angulo: "evidencia"
mitre: ""
owasp: ""
tags: ["18-evasion", "purple-detect", "evidencia"]
aliases: ["EDR bypass discussion ética", "edr-bypass", "edr-bypass-evidencia"]
---

# EDR bypass discussion ética — evidência

Pacote pra EDR bypass discussion ética sobreviver peer review.

## Contexto

Purple team de qualidade executa técnicas com telemetria pré-combinada e mede
cobertura (True Positive, gap, alerta que não veio). O entregável de valor é a
matriz ATT&CK + evidência de alerta — não apenas a execução do payload.

## O que precisa aparecer

- Detalhe que pago pra ver: **Sem malware crimeware**.

## Checklist

Sem pacote completo o finding vira pingue-pongue no reteste.

## Mínimo que eu aceito

Matriz técnica→alerta; screenshots SIEM; recomendações.

## Exemplo

```http
HTTP/1.1 200 OK
Content-Type: application/json
X-Request-Id: 4ac94a

{"id":"ORD-7781","owner":"USER_A","note":"redacted-edr-bypass"}
# capturado como USER_B
```

## Remediação junto

Fechar gaps com rules; data sources faltantes; tuning.

## Se purple

Métricas de cobertura ATT&CK; mean time to alert.

## Armadilha

Não desabilito EDR para 'passar'. Documento bypass se no escopo.

## Refs

- [MITRE ATT&CK](https://attack.mitre.org/)
- [Atomic Red Team](https://github.com/redcanaryco/atomic-red-team)
- [SigmaHQ rules](https://github.com/SigmaHQ/sigma)

## Relacionadas

- [EDR bypass discussion ética](0343-purple-detect-edr-bypass.md)
- [Atomic Red Team na prática](0341-purple-detect-atomic.md)
- [canary tokens validation](0349-purple-detect-canary.md)
- [CloudTrail gaps](0345-purple-detect-cloudtrail.md)
- [DNS anomaly detection test](0346-purple-detect-dns-dga.md)