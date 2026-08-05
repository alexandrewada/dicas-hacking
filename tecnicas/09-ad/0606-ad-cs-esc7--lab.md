---
id: "0606"
categoria: "09-ad"
familia: "ad-cs"
slug: "esc7"
angulo: "lab"
mitre: ""
owasp: ""
tags: ["09-ad", "ad-cs", "lab"]
aliases: ["ESC7 ManageCA", "esc7", "esc7-lab"]
---

# ESC7 ManageCA — lab

Lab só pra ESC7 ManageCA. Se não reproduz isolado, não confio no finding de prod.

## Contexto

Active Directory Certificate Services introduziu uma classe moderna de takeover (ESC1–ESC8+).
Templates com client auth + enrollee supplies subject permitem impersonation.
Relay para HTTP enrollment (ESC8) combina com coerção. Conteúdo obrigatório em AD moderno.

## Variante

- Template + enrollee + EKU + manager approval. Cito a misconfig, não 'ADCS vulnerable'.

## Setup

VM/conta throwaway na versão parecida.
Snapshot antes.
Cleanup escrito antes de explorar.

## Fluxo

1. Enumero CA e templates (certipy/certify) no escopo.
2. Identifico ESC1/2/3/4/6/7/8 aplicáveis.
3. Emito certificado de conta de teste / path autorizado.
4. Autentico via PKINIT/Schannel conforme caso.
5. Revogo cert de teste e reporto templates.

## PoC mínimo

```bash
# AD CS esc7 — enum + request mínimo no lab
certipy find -u USER_A@lab.local -p PASS_LAB -dc-ip DC01.lab.local -vulnerable
certipy req -u USER_A@lab.local -p PASS_LAB -ca LAB-CA -template TPL_esc7 -out esc7_9ad2e5
```

## Pitfall

Certificados são persistência — revogo sempre ao final.
Não emito cert para Domain Admin real sem acordo explícito.

Ritmo no KDC/LDAP. Conta low-priv. Zero mudança destrutiva em objeto prod sem janela.

## Prova do lab

Template vulnerável; cert de teste; auth proof; revogação.

## Refs

- [SpecterOps — Certified Pre-Owned (AD CS)](https://posts.specterops.io/certified-pre-owned-d95910965cd2)
- [MITRE ATT&CK T1649](https://attack.mitre.org/techniques/T1649/)

## Relacionadas

- [ESC7 ManageCA](0226-ad-cs-esc7.md)
- [ESC7 ManageCA — hardening](0986-ad-cs-esc7--hardening.md)
- [AD CS ESC1](0221-ad-cs-esc1.md)
- [AD CS ESC8 (relay HTTP)](0227-ad-cs-esc8.md)
- [persistência via certs](0229-ad-cs-persist.md)
- [detecção de enrollment anômalo](0230-ad-cs-detect.md)