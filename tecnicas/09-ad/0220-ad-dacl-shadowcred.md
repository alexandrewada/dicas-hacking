---
id: "0220"
categoria: "09-ad"
familia: "ad-dacl"
slug: "shadowcred"
angulo: "base"
mitre: ""
owasp: ""
tags: ["09-ad", "ad-dacl", "base"]
aliases: ["KeyCredentialLink / Shadow Credentials", "shadowcred"]
---

# KeyCredentialLink / Shadow Credentials

## Leitura rápida

BloodHound popularizou edges: GenericAll, WriteDACL, ForceChangePassword, DCSync rights,
AddMember, etc. valida o caminho em lab controlado e prova com ação mínima
(reset de conta teste, add a grupo lab), não com destruição.

## Foco

- **PKINIT abuse** — muda ruído e o que entra no PDF.

## Mãos na massa

1. Coleto dados BloodHound com credencial autorizada.
2. Analisar paths até Dualidade DA/Tier0.
3. Valido ACEs exploráveis com ação mínima.
4. Documento objeto, ACE e impacto.
5. Propor remediação (remove ACE, tiering).

## PoC mínimo

```bash
# DACL shadowcred — prova de ACE sem mudança destrutiva
bloodyAD --host DC01.lab.local -d lab.local -u USER_A -p PASS_LAB \
  get object 'CN=TARGET_OBJ,OU=Lab,DC=lab,DC=local' --attr nTSecurityDescriptor
# edge esperado: shadowcred → conta teste; tag 07e3c1
```

Path até tier0 com ACE/edge exato (GenericAll, WriteDacl, ForceChangePassword). 'Deu certo' sem grafo não fecha.

## Pitfall

DCSync em produção é sensível — alinhe com cliente.
Evito resetar senhas de usuários reais.

## Detecção / remediação

Directory Services Changes auditing; BloodHound Enterprise-like monitoring.

→ AdminSDHolder higiene; least privilege; Privileged Access Workstations;
remover ACEs excessivos.

## Prova

Edge BloodHound; PoC controlado; ACE dump.

## Refs

- [SpecterOps — BloodHound docs](https://bloodhound.specterops.io/)
- [MITRE ATT&CK](https://attack.mitre.org/)
- [MITRE ATT&CK T1484](https://attack.mitre.org/techniques/T1484/)

## Relacionadas

- [KeyCredentialLink / Shadow Credentials — lab](0600-ad-dacl-shadowcred--lab.md)
- [KeyCredentialLink / Shadow Credentials — hardening](0980-ad-dacl-shadowcred--hardening.md)
- [GenericAll em usuário/grupo](0211-ad-dacl-genericall.md)
- [Direitos de DCSync](0213-ad-dacl-dcsync.md)
- [WriteSPN → targeted roast](0216-ad-dacl-writespn.md)
- [AD CS ESC1 (path)](0221-ad-cs-esc1.md)