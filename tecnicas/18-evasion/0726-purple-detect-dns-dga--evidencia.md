---
id: "0726"
categoria: "18-evasion"
familia: "purple-detect"
slug: "dns-dga"
angulo: "evidencia"
mitre: ""
owasp: ""
tags: ["18-evasion", "purple-detect", "evidencia"]
aliases: ["DNS anomaly detection test", "dns-dga", "dns-dga-evidencia"]
---

# DNS anomaly detection test — evidência

Pacote pra DNS anomaly detection test sobreviver peer review.

## Contexto

Purple team de qualidade executa técnicas com telemetria pré-combinada e mede
cobertura (True Positive, gap, alerta que não veio). O entregável de valor é a
matriz ATT&CK + evidência de alerta — não apenas a execução do payload.

## O que precisa aparecer

- Variante DNS anomaly detection test: trato separado da família `purple-detect`.

## Checklist

- ROE cobre
- ambiente/versão
- identidade de teste
- PoC redigido
- impacto 2–3 frases
- hotfix + estrutural
- cleanup
- MITRE/OWASP

## Mínimo que eu aceito

Matriz técnica→alerta; screenshots SIEM; recomendações.

## No lab ficou assim

```http
HTTP/1.1 200 OK
Content-Type: application/json
X-Request-Id: c22266

{"id":"a1b2c3d4-e5f6-7890-abcd-ef1234567890","owner":"USER_A","note":"redacted-dns-dga"}
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

- [DNS anomaly detection test](0346-purple-detect-dns-dga.md)
- [Atomic Red Team na prática](0341-purple-detect-atomic.md)
- [canary tokens validation](0349-purple-detect-canary.md)
- [CloudTrail gaps](0345-purple-detect-cloudtrail.md)
- [EDR bypass discussion ética](0343-purple-detect-edr-bypass.md)