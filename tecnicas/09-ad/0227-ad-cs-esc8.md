---
id: "0227"
categoria: "09-ad"
familia: "ad-cs"
slug: "esc8"
angulo: "base"
mitre: "T1649"
owasp: ""
tags: ["09-ad", "ad-cs", "base", "t1649"]
aliases: ["AD CS ESC8 (relay HTTP)", "esc8"]
---

# AD CS ESC8 (relay HTTP)

**Identity** · `T1649 Steal or Forge Authentication Certificates`

Active Directory Certificate Services introduziu uma classe moderna de takeover (ESC1–ESC8+).
Templates com client auth + enrollee supplies subject permitem impersonation.
Relay para HTTP enrollment (ESC8) combina com coerção. Conteúdo obrigatório em AD moderno.

**Variante:** Signing/EPA/channel binding decidem se o relay vive. Template + enrollee + EKU + manager approval. Cito a misconfig, não 'ADCS vulnerable'.

**Método**

1. Enumero CA e templates (certipy/certify) no escopo.
2. Identifico ESC1/2/3/4/6/7/8 aplicáveis.
3. Emito certificado de conta de teste / path autorizado.
4. Autentico via PKINIT/Schannel conforme caso.
5. Revogo cert de teste e reporto templates.

## No lab ficou assim

```bash
# AD CS esc8 — enum + request mínimo no lab
certipy find -u USER_A@lab.local -p PASS_LAB -dc-ip DC01.lab.local -vulnerable
certipy req -u USER_A@lab.local -p PASS_LAB -ca LAB-CA -template TPL_esc8 -out esc8_fb9311
```

**Freio:** Certificados são persistência — revogo sempre ao final.

Já abri High demais em ESC8 NTLM relay to HTTP por sintoma sem efeito. Cruzei com: Monitor certificate issuance; template change audits; CA enrollment logs. Sem side-effect, baixo.

Detecto via: Monitor certificate issuance; template change audits; CA enrollment logs.

Corrijo com: Corrigir templates; manager approval; restringir enrollment;
proteger HTTP enrollment; EPA.

Levo no report: Template vulnerável; cert de teste; auth proof; revogação.

## Refs

- [MITRE ATT&CK T1649](https://attack.mitre.org/techniques/T1649/)
- [SpecterOps — Certified Pre-Owned (AD CS)](https://posts.specterops.io/certified-pre-owned-d95910965cd2)

## Relacionadas

- [AD CS ESC8 (relay HTTP) — lab](0607-ad-cs-esc8--lab.md)
- [AD CS ESC8 (relay HTTP) — hardening](0987-ad-cs-esc8--hardening.md)
- [AD CS ESC1](0221-ad-cs-esc1.md)
- [persistência via certs](0229-ad-cs-persist.md)
- [detecção de enrollment anômalo](0230-ad-cs-detect.md)
- [coerção + relay (path)](../08-network/0186-net-llmnr-nbt-petitpotam.md)
- [Direitos de DCSync (path)](0213-ad-dacl-dcsync.md)