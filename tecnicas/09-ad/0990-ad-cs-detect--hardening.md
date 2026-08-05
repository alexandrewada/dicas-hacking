---
id: "0990"
categoria: "09-ad"
familia: "ad-cs"
slug: "detect"
angulo: "hardening"
mitre: "T1649"
owasp: ""
tags: ["09-ad", "ad-cs", "hardening", "t1649"]
aliases: ["detecção de enrollment anômalo", "detect", "detect-hardening"]
---

# detecção de enrollment anômalo — hardening

Do PoC ao controle — detecção de enrollment anômalo.

## Risco

Active Directory Certificate Services introduziu uma classe moderna de takeover (ESC1–ESC8+).
Templates com client auth + enrollee supplies subject permitem impersonation.
Relay para HTTP enrollment (ESC8) combina com coerção. Conteúdo obrigatório em AD moderno.

## Controles desta variante

- **Purple.** Sem isso o playbook da família mente.
- Template + enrollee + EKU + manager approval. Cito a misconfig, não 'ADCS vulnerable'.

## Camadas

Controle que fecha: Corrigir templates; manager approval; restringir enrollment;
proteger HTTP enrollment; EPA.
Sinal que deveria existir: Monitor certificate issuance; template change audits; CA enrollment logs.

## PoC mínimo

```text
antes: controle ausente para detect
depois: ownership check / deny default em TARGET
verificação: PoC 72e414 retorna 403/blocked
reteste USER_A vs USER_B
```

## Armadilha

Certificados são persistência — revogo sempre ao final.
Não emito cert para Domain Admin real sem acordo explícito.

## Antes/depois

Template vulnerável; cert de teste; auth proof; revogação.

Aceite de risco só por escrito, com prazo.

## Refs

- [MITRE ATT&CK T1649](https://attack.mitre.org/techniques/T1649/)
- [SpecterOps — Certified Pre-Owned (AD CS)](https://posts.specterops.io/certified-pre-owned-d95910965cd2)

## Relacionadas

- [detecção de enrollment anômalo](0230-ad-cs-detect.md)
- [detecção de enrollment anômalo — lab](0610-ad-cs-detect--lab.md)
- [AD CS ESC1](0221-ad-cs-esc1.md)
- [AD CS ESC8 (relay HTTP)](0227-ad-cs-esc8.md)
- [persistência via certs](0229-ad-cs-persist.md)