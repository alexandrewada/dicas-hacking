---
id: "0983"
categoria: "09-ad"
familia: "ad-cs"
slug: "esc3"
angulo: "hardening"
mitre: "T1649"
owasp: ""
tags: ["09-ad", "ad-cs", "hardening", "t1649"]
aliases: ["ESC3 enrollment agent", "esc3", "esc3-hardening"]
---

# ESC3 enrollment agent — hardening

Do PoC ao controle — ESC3 enrollment agent.

## Risco

Active Directory Certificate Services introduziu uma classe moderna de takeover (ESC1–ESC8+).
Templates com client auth + enrollee supplies subject permitem impersonation.
Relay para HTTP enrollment (ESC8) combina com coerção. Conteúdo obrigatório em AD moderno.

## Controles desta variante

- Template + enrollee + EKU + manager approval. Cito a misconfig, não 'ADCS vulnerable'.

## Camadas

Controle que fecha: Corrigir templates; manager approval; restringir enrollment;
proteger HTTP enrollment; EPA.
Sinal que deveria existir: Monitor certificate issuance; template change audits; CA enrollment logs.

## No lab ficou assim

```bash
# verificação pós-hardening esc3
curl -sk -o /dev/null -w '%{http_code}\n' https://app.lab.local/esc3/10042 \
  -H 'Cookie: session=USER_B'
# esperado 403 — tag 722288
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

- [ESC3 enrollment agent](0223-ad-cs-esc3.md)
- [ESC3 enrollment agent — lab](0603-ad-cs-esc3--lab.md)
- [AD CS ESC1](0221-ad-cs-esc1.md)
- [AD CS ESC8 (relay HTTP)](0227-ad-cs-esc8.md)
- [persistência via certs](0229-ad-cs-persist.md)
- [detecção de enrollment anômalo](0230-ad-cs-detect.md)