---
id: "0987"
categoria: "09-ad"
familia: "ad-cs"
slug: "esc8"
angulo: "hardening"
mitre: "T1649"
owasp: ""
tags: ["09-ad", "ad-cs", "hardening", "t1649"]
aliases: ["AD CS ESC8 (relay HTTP)", "esc8", "esc8-hardening"]
---

# AD CS ESC8 (relay HTTP) — hardening

Do PoC ao controle — AD CS ESC8 (relay HTTP).

## Risco

Active Directory Certificate Services introduziu uma classe moderna de takeover (ESC1–ESC8+).
Templates com client auth + enrollee supplies subject permitem impersonation.
Relay para HTTP enrollment (ESC8) combina com coerção. Conteúdo obrigatório em AD moderno.

## Controles desta variante

- Signing/EPA/channel binding decidem se o relay vive.
- Template + enrollee + EKU + manager approval. Cito a misconfig, não 'ADCS vulnerable'.

## Camadas

1) Bloqueio imediato
2) Monitor certificate issuance; template change audits; CA enrollment logs.
3) Corrigir templates; manager approval; restringir enrollment;
proteger HTTP enrollment; EPA.
Reteste com o mesmo PoC — critério: a prova desta variante falha.

## Exemplo

```bash
# verificação pós-hardening esc8
curl -sk -o /dev/null -w '%{http_code}\n' https://app.lab.local/esc8/obj_c248ac \
  -H 'Cookie: session=USER_B'
# esperado 403 — tag c248ac
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

- [AD CS ESC8 (relay HTTP)](0227-ad-cs-esc8.md)
- [AD CS ESC8 (relay HTTP) — lab](0607-ad-cs-esc8--lab.md)
- [AD CS ESC1](0221-ad-cs-esc1.md)
- [persistência via certs](0229-ad-cs-persist.md)
- [detecção de enrollment anômalo](0230-ad-cs-detect.md)
- [coerção + relay (path)](../08-network/0186-net-llmnr-nbt-petitpotam.md)
- [Direitos de DCSync (path)](0213-ad-dacl-dcsync.md)