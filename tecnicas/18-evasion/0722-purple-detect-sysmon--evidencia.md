---
id: "0722"
categoria: "18-evasion"
familia: "purple-detect"
slug: "sysmon"
angulo: "evidencia"
mitre: ""
owasp: ""
tags: ["18-evasion", "purple-detect", "evidencia"]
aliases: ["Sysmon coverage gaps", "sysmon", "sysmon-evidencia"]
---

# Sysmon coverage gaps — evidência

Pacote pra Sysmon coverage gaps sobreviver peer review.

## Contexto

Purple team de qualidade executa técnicas com telemetria pré-combinada e mede
cobertura (True Positive, gap, alerta que não veio). O entregável de valor é a
matriz ATT&CK + evidência de alerta — não apenas a execução do payload.

## O que precisa aparecer

- Variante Sysmon coverage gaps: trato separado da família `purple-detect`.

## Checklist

Sem pacote completo o finding vira pingue-pongue no reteste.

## Mínimo que eu aceito

Matriz técnica→alerta; screenshots SIEM; recomendações.

## Exemplo

```http
HTTP/1.1 200 OK
Content-Type: application/json
X-Request-Id: c144f1

{"id":"usr_01HZX","owner":"USER_A","note":"redacted-sysmon"}
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

- [Sysmon coverage gaps](0342-purple-detect-sysmon.md)
- [Atomic Red Team na prática](0341-purple-detect-atomic.md)
- [canary tokens validation](0349-purple-detect-canary.md)
- [CloudTrail gaps](0345-purple-detect-cloudtrail.md)
- [DNS anomaly detection test](0346-purple-detect-dns-dga.md)