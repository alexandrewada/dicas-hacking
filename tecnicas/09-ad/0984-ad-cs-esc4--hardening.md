---
id: "0984"
categoria: "09-ad"
familia: "ad-cs"
slug: "esc4"
angulo: "hardening"
mitre: "T1649"
owasp: ""
tags: ["09-ad", "ad-cs", "hardening", "t1649"]
aliases: ["ESC4 template ACL write", "esc4", "esc4-hardening"]
---

# ESC4 template ACL write — hardening

Do PoC ao controle — ESC4 template ACL write.

## Risco

Active Directory Certificate Services introduziu uma classe moderna de takeover (ESC1–ESC8+).
Templates com client auth + enrollee supplies subject permitem impersonation.
Relay para HTTP enrollment (ESC8) combina com coerção. Conteúdo obrigatório em AD moderno.

## Controles desta variante

- Exporto shortest path até tier0 com o edge exato. Sem isso a remediação vira 'olha o BloodHound'.
- Template + enrollee + EKU + manager approval. Cito a misconfig, não 'ADCS vulnerable'.

## Camadas

1) Bloqueio imediato
2) Monitor certificate issuance; template change audits; CA enrollment logs.
3) Corrigir templates; manager approval; restringir enrollment;
proteger HTTP enrollment; EPA.
Reteste com o mesmo PoC — critério: a prova desta variante falha.

## PoC mínimo

```text
antes: controle ausente para esc4
depois: ownership check / deny default em TARGET
verificação: PoC 05b11e retorna 403/blocked
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

- [ESC4 template ACL write](0224-ad-cs-esc4.md)
- [ESC4 template ACL write — lab](0604-ad-cs-esc4--lab.md)
- [AD CS ESC1](0221-ad-cs-esc1.md)
- [AD CS ESC8 (relay HTTP)](0227-ad-cs-esc8.md)
- [persistência via certs](0229-ad-cs-persist.md)
- [detecção de enrollment anômalo](0230-ad-cs-detect.md)