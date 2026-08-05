---
id: "0724"
categoria: "18-evasion"
familia: "purple-detect"
slug: "sigma"
angulo: "evidencia"
mitre: ""
owasp: ""
tags: ["18-evasion", "purple-detect", "evidencia"]
aliases: ["sugerir regra Sigma", "sigma", "sigma-evidencia"]
---

# sugerir regra Sigma — evidência

Pacote pra sugerir regra Sigma sobreviver peer review.

## Contexto

Purple team de qualidade executa técnicas com telemetria pré-combinada e mede
cobertura (True Positive, gap, alerta que não veio). O entregável de valor é a
matriz ATT&CK + evidência de alerta — não apenas a execução do payload.

## O que precisa aparecer

- Detalhe que pago pra ver: **Entrega defensiva**.

## Checklist

Sem pacote completo o finding vira pingue-pongue no reteste.

## Mínimo que eu aceito

Matriz técnica→alerta; screenshots SIEM; recomendações.

## Exemplo

```http
HTTP/1.1 200 OK
Content-Type: application/json
X-Request-Id: a3bc98

{"id":"ORD-7781","owner":"USER_A","note":"redacted-sigma"}
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

- [sugerir regra Sigma](0344-purple-detect-sigma.md)
- [Atomic Red Team na prática](0341-purple-detect-atomic.md)
- [canary tokens validation](0349-purple-detect-canary.md)
- [CloudTrail gaps](0345-purple-detect-cloudtrail.md)
- [DNS anomaly detection test](0346-purple-detect-dns-dga.md)