---
id: "0609"
categoria: "09-ad"
familia: "ad-cs"
slug: "persist"
angulo: "lab"
mitre: ""
owasp: ""
tags: ["09-ad", "ad-cs", "lab"]
aliases: ["persistência via certs", "persist", "persist-lab"]
---

# persistência via certs — lab

Sandbox throwaway — persistência via certs sem ruído de cliente.

## Contexto

Active Directory Certificate Services introduziu uma classe moderna de takeover (ESC1–ESC8+).
Templates com client auth + enrollee supplies subject permitem impersonation.
Relay para HTTP enrollment (ESC8) combina com coerção. Conteúdo obrigatório em AD moderno.

## Variante

- Se não validar **Client auth long-lived**, a nota fica genérica.
- Template + enrollee + EKU + manager approval. Cito a misconfig, não 'ADCS vulnerable'.

## Setup

Ativo mínimo. Duas identidades se for authz.
Restore point.

## Fluxo

1. Enumero CA e templates (certipy/certify) no escopo.
2. Identifico ESC1/2/3/4/6/7/8 aplicáveis.
3. Emito certificado de conta de teste / path autorizado.
4. Autentico via PKINIT/Schannel conforme caso.
5. Revogo cert de teste e reporto templates.

## Exemplo

```bash
# AD CS persist — lab CA, conta teste
certipy find -u USER_A@lab.local -p PASS_LAB -dc-ip DC01.lab.local -vulnerable
# persist: renovar cert de conta teste; detect: correlacionar 4886→4768
# tag 1f4db4 — sem shadow em prod
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

- [persistência via certs](0229-ad-cs-persist.md)
- [persistência via certs — hardening](0989-ad-cs-persist--hardening.md)
- [AD CS ESC1](0221-ad-cs-esc1.md)
- [AD CS ESC8 (relay HTTP)](0227-ad-cs-esc8.md)
- [detecção de enrollment anômalo](0230-ad-cs-detect.md)