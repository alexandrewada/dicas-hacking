---
id: "0989"
categoria: "09-ad"
familia: "ad-cs"
slug: "persist"
angulo: "hardening"
mitre: ""
owasp: ""
tags: ["09-ad", "ad-cs", "hardening"]
aliases: ["persistência via certs", "persist", "persist-hardening"]
---

# persistência via certs — hardening

Do PoC ao controle — persistência via certs.

## Risco

Active Directory Certificate Services introduziu uma classe moderna de takeover (ESC1–ESC8+).
Templates com client auth + enrollee supplies subject permitem impersonation.
Relay para HTTP enrollment (ESC8) combina com coerção. Conteúdo obrigatório em AD moderno.

## Controles desta variante

- Se não validar **Client auth long-lived**, a nota fica genérica.
- Template + enrollee + EKU + manager approval. Cito a misconfig, não 'ADCS vulnerable'.

## Camadas

1) Bloqueio imediato
2) Monitor certificate issuance; template change audits; CA enrollment logs.
3) Corrigir templates; manager approval; restringir enrollment;
proteger HTTP enrollment; EPA.
Reteste com o mesmo PoC — critério: a prova desta variante falha.

## Exemplo

```bash
# verificação pós-hardening persist
curl -sk -o /dev/null -w '%{http_code}\n' https://app.lab.local/persist/obj_ed8245 \
  -H 'Cookie: session=USER_B'
# esperado 403 — tag ed8245
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

- [persistência via certs](0229-ad-cs-persist.md)
- [persistência via certs — lab](0609-ad-cs-persist--lab.md)
- [AD CS ESC1](0221-ad-cs-esc1.md)
- [AD CS ESC8 (relay HTTP)](0227-ad-cs-esc8.md)
- [detecção de enrollment anômalo](0230-ad-cs-detect.md)