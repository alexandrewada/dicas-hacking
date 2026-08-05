---
id: "0229"
categoria: "09-ad"
familia: "ad-cs"
slug: "persist"
angulo: "base"
mitre: ""
owasp: ""
tags: ["09-ad", "ad-cs", "base"]
aliases: ["persistência via certs", "persist"]
---

# persistência via certs

## Leitura rápida

Active Directory Certificate Services introduziu uma classe moderna de takeover (ESC1–ESC8+).
Templates com client auth + enrollee supplies subject permitem impersonation.
Relay para HTTP enrollment (ESC8) combina com coerção. Conteúdo obrigatório em AD moderno.

## Foco

- Se não validar **Client auth long-lived**, a nota fica genérica.
- Template + enrollee + EKU + manager approval. Cito a misconfig, não 'ADCS vulnerable'.

## Mãos na massa

1. Enumero CA e templates (certipy/certify) no escopo.
2. Identifico ESC1/2/3/4/6/7/8 aplicáveis.
3. Emito certificado de conta de teste / path autorizado.
4. Autentico via PKINIT/Schannel conforme caso.
5. Revogo cert de teste e reporto templates.

## No lab ficou assim

```bash
# AD CS persist — lab CA, conta teste
certipy find -u USER_A@lab.local -p PASS_LAB -dc-ip DC01.lab.local -vulnerable
# persist: renovar cert de conta teste; detect: correlacionar 4886→4768
# tag c32af2 — sem shadow em prod
```

Ritmo no KDC/LDAP. Conta low-priv. Zero mudança destrutiva em objeto prod sem janela.

## Pitfall

Certificados são persistência — revogo sempre ao final.
Não emito cert para Domain Admin real sem acordo explícito.

## Detecção / remediação

Monitor certificate issuance; template change audits; CA enrollment logs.

→ Corrigir templates; manager approval; restringir enrollment;
proteger HTTP enrollment; EPA.

## Prova

Template vulnerável; cert de teste; auth proof; revogação.

## Refs

- [SpecterOps — Certified Pre-Owned (AD CS)](https://posts.specterops.io/certified-pre-owned-d95910965cd2)
- [MITRE ATT&CK T1649](https://attack.mitre.org/techniques/T1649/)

## Relacionadas

- [persistência via certs — lab](0609-ad-cs-persist--lab.md)
- [persistência via certs — hardening](0989-ad-cs-persist--hardening.md)
- [AD CS ESC1](0221-ad-cs-esc1.md)
- [AD CS ESC8 (relay HTTP)](0227-ad-cs-esc8.md)
- [detecção de enrollment anômalo](0230-ad-cs-detect.md)