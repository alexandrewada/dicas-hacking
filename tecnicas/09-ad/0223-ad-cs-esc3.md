---
id: "0223"
categoria: "09-ad"
familia: "ad-cs"
slug: "esc3"
angulo: "base"
mitre: "T1649"
owasp: ""
tags: ["09-ad", "ad-cs", "base", "t1649"]
aliases: ["ESC3 enrollment agent", "esc3"]
---

# ESC3 enrollment agent

**Identity** · `T1649 Steal or Forge Authentication Certificates`

## Contexto

Active Directory Certificate Services introduziu uma classe moderna de takeover (ESC1–ESC8+).
Templates com client auth + enrollee supplies subject permitem impersonation.
Relay para HTTP enrollment (ESC8) combina com coerção. Conteúdo obrigatório em AD moderno.

## O que muda aqui

- Template + enrollee + EKU + manager approval. Cito a misconfig, não 'ADCS vulnerable'.

## Como testo

1. Enumero CA e templates (certipy/certify) no escopo.
2. Identifico ESC1/2/3/4/6/7/8 aplicáveis.
3. Emito certificado de conta de teste / path autorizado.
4. Autentico via PKINIT/Schannel conforme caso.
5. Revogo cert de teste e reporto templates.

## No lab ficou assim

```bash
# AD CS esc3 — enum + request mínimo no lab
certipy find -u USER_A@lab.local -p PASS_LAB -dc-ip DC01.lab.local -vulnerable
certipy req -u USER_A@lab.local -p PASS_LAB -ca LAB-CA -template TPL_esc3 -out esc3_2a59a9
```

## Campo

Ritmo no KDC/LDAP. Conta low-priv. Zero mudança destrutiva em objeto prod sem janela.

Antes de Critical em ESC3 enrollment agent, confiro se a telemetria que eu cobraria reagiria — Monitor certificate issuance; template change audits; CA enrollment logs.

## Já me queimei

Certificados são persistência — revogo sempre ao final.
Não emito cert para Domain Admin real sem acordo explícito.

## Blue

- Detectar: Monitor certificate issuance; template change audits; CA enrollment logs.
- Fechar: Corrigir templates; manager approval; restringir enrollment;
proteger HTTP enrollment; EPA.

## Evidência

Template vulnerável; cert de teste; auth proof; revogação.

## Refs

- [MITRE ATT&CK T1649](https://attack.mitre.org/techniques/T1649/)
- [SpecterOps — Certified Pre-Owned (AD CS)](https://posts.specterops.io/certified-pre-owned-d95910965cd2)

## Relacionadas

- [ESC3 enrollment agent — lab](0603-ad-cs-esc3--lab.md)
- [ESC3 enrollment agent — hardening](0983-ad-cs-esc3--hardening.md)
- [AD CS ESC1](0221-ad-cs-esc1.md)
- [AD CS ESC8 (relay HTTP)](0227-ad-cs-esc8.md)
- [persistência via certs](0229-ad-cs-persist.md)
- [detecção de enrollment anômalo](0230-ad-cs-detect.md)