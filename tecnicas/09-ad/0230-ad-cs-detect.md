---
id: "0230"
categoria: "09-ad"
familia: "ad-cs"
slug: "detect"
angulo: "base"
mitre: "T1649"
owasp: ""
tags: ["09-ad", "ad-cs", "base", "t1649"]
aliases: ["detecção de enrollment anômalo", "detect"]
---

# detecção de enrollment anômalo

**Identity** · `T1649 Steal or Forge Authentication Certificates`

## Contexto

Active Directory Certificate Services introduziu uma classe moderna de takeover (ESC1–ESC8+).
Templates com client auth + enrollee supplies subject permitem impersonation.
Relay para HTTP enrollment (ESC8) combina com coerção. Conteúdo obrigatório em AD moderno.

## O que muda aqui

- **Purple.** Sem isso o playbook da família mente.
- Template + enrollee + EKU + manager approval. Cito a misconfig, não 'ADCS vulnerable'.

## Como testo

1. Enumero CA e templates (certipy/certify) no escopo.
2. Identifico ESC1/2/3/4/6/7/8 aplicáveis.
3. Emito certificado de conta de teste / path autorizado.
4. Autentico via PKINIT/Schannel conforme caso.
5. Revogo cert de teste e reporto templates.

## PoC mínimo

```bash
# AD CS detect — lab CA, conta teste
certipy find -u USER_A@lab.local -p PASS_LAB -dc-ip DC01.lab.local -vulnerable
# persist: renovar cert de conta teste; detect: correlacionar 4886→4768
# tag 4d8b13 — sem shadow em prod
```

## Campo

Path até tier0 com ACE/edge exato (GenericAll, WriteDacl, ForceChangePassword). 'Deu certo' sem grafo não fecha.

Falso amigo em detecção de enrollment anômalo: UI/log gritam, impacto não. Exijo Monitor certificate issuance.

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

- [detecção de enrollment anômalo — lab](0610-ad-cs-detect--lab.md)
- [detecção de enrollment anômalo — hardening](0990-ad-cs-detect--hardening.md)
- [AD CS ESC1](0221-ad-cs-esc1.md)
- [AD CS ESC8 (relay HTTP)](0227-ad-cs-esc8.md)
- [persistência via certs](0229-ad-cs-persist.md)