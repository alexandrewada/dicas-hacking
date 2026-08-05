---
id: "0725"
categoria: "18-evasion"
familia: "purple-detect"
slug: "cloudtrail"
angulo: "evidencia"
mitre: ""
owasp: ""
tags: ["18-evasion", "purple-detect", "evidencia"]
aliases: ["CloudTrail gaps", "cloudtrail", "cloudtrail-evidencia"]
---

# CloudTrail gaps — evidência

Pacote pra CloudTrail gaps sobreviver peer review.

## Contexto

Purple team de qualidade executa técnicas com telemetria pré-combinada e mede
cobertura (True Positive, gap, alerta que não veio). O entregável de valor é a
matriz ATT&CK + evidência de alerta — não apenas a execução do payload.

## O que precisa aparecer

- Variante CloudTrail gaps: trato separado da família `purple-detect`.

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

## PoC mínimo

```text
--- evidência redigida ---
req: GET /…/ORD-7781 Cookie=USER_B
res: 200 body_len=412 fields=[email,role] # PII mascarada
impacto: leitura cross-user (cloudtrail)
hash_prova: ae60b3
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

- [CloudTrail gaps](0345-purple-detect-cloudtrail.md)
- [Atomic Red Team na prática](0341-purple-detect-atomic.md)
- [canary tokens validation](0349-purple-detect-canary.md)
- [DNS anomaly detection test](0346-purple-detect-dns-dga.md)
- [EDR bypass discussion ética](0343-purple-detect-edr-bypass.md)