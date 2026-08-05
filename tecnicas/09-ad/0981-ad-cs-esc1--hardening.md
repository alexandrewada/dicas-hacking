---
id: "0981"
categoria: "09-ad"
familia: "ad-cs"
slug: "esc1"
angulo: "hardening"
mitre: ""
owasp: ""
tags: ["09-ad", "ad-cs", "hardening"]
aliases: ["AD CS ESC1", "esc1", "esc1-hardening"]
---

# AD CS ESC1 — hardening

Do PoC ao controle — AD CS ESC1.

## Risco

Active Directory Certificate Services introduziu uma classe moderna de takeover (ESC1–ESC8+).
Templates com client auth + enrollee supplies subject permitem impersonation.
Relay para HTTP enrollment (ESC8) combina com coerção. Conteúdo obrigatório em AD moderno.

## Controles desta variante

- Detalhe que pago pra ver: **Client auth EKU**.
- Template + enrollee + EKU + manager approval. Cito a misconfig, não 'ADCS vulnerable'.

## Camadas

1) Bloqueio imediato
2) Monitor certificate issuance; template change audits; CA enrollment logs.
3) Corrigir templates; manager approval; restringir enrollment;
proteger HTTP enrollment; EPA.
Reteste com o mesmo PoC — critério: a prova desta variante falha.

## Exemplo

```text
checklist esc1:
- [ ] controle preventivo ativo
- [ ] telemetria cobre o PoC
- [ ] reteste com mesma prova (363ee1) falha
```

## Armadilha

Certificados são persistência — revogo sempre ao final.
Não emito cert para Domain Admin real sem acordo explícito.

## Antes/depois

Template vulnerável; cert de teste; auth proof; revogação.

Aceite de risco só por escrito, com prazo.

## Refs

- [SpecterOps — Certified Pre-Owned (AD CS)](https://posts.specterops.io/certified-pre-owned-d95910965cd2)
- [MITRE ATT&CK T1649](https://attack.mitre.org/techniques/T1649/)

## Relacionadas

- [AD CS ESC1](0221-ad-cs-esc1.md)
- [AD CS ESC1 — lab](0601-ad-cs-esc1--lab.md)
- [AD CS ESC8 (relay HTTP)](0227-ad-cs-esc8.md)
- [persistência via certs](0229-ad-cs-persist.md)
- [detecção de enrollment anômalo](0230-ad-cs-detect.md)
- [Direitos de DCSync (path)](0213-ad-dacl-dcsync.md)