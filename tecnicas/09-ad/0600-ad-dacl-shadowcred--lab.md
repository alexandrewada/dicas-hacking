---
id: "0600"
categoria: "09-ad"
familia: "ad-dacl"
slug: "shadowcred"
angulo: "lab"
mitre: ""
owasp: ""
tags: ["09-ad", "ad-dacl", "lab"]
aliases: ["KeyCredentialLink / Shadow Credentials", "shadowcred", "shadowcred-lab"]
---

# KeyCredentialLink / Shadow Credentials — lab

Lab só pra KeyCredentialLink / Shadow Credentials. Se não reproduz isolado, não confio no finding de prod.

## Contexto

BloodHound popularizou edges: GenericAll, WriteDACL, ForceChangePassword, DCSync rights,
AddMember, etc. valida o caminho em lab controlado e prova com ação mínima
(reset de conta teste, add a grupo lab), não com destruição.

## Variante

- **PKINIT abuse** — muda ruído e o que entra no PDF.

## Setup

VM/conta throwaway na versão parecida.
Snapshot antes.
Cleanup escrito antes de explorar.

## Fluxo

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
# edge esperado: shadowcred → conta teste; tag 70d3c7
```

## Pitfall

DCSync em produção é sensível — alinhe com cliente.
Evito resetar senhas de usuários reais.

Path até tier0 com ACE/edge exato (GenericAll, WriteDacl, ForceChangePassword). 'Deu certo' sem grafo não fecha.

## Prova do lab

Edge BloodHound; PoC controlado; ACE dump.

## Refs

- [SpecterOps — BloodHound docs](https://bloodhound.specterops.io/)
- [MITRE ATT&CK](https://attack.mitre.org/)
- [MITRE ATT&CK T1484](https://attack.mitre.org/techniques/T1484/)

## Relacionadas

- [KeyCredentialLink / Shadow Credentials](0220-ad-dacl-shadowcred.md)
- [KeyCredentialLink / Shadow Credentials — hardening](0980-ad-dacl-shadowcred--hardening.md)
- [GenericAll em usuário/grupo](0211-ad-dacl-genericall.md)
- [Direitos de DCSync](0213-ad-dacl-dcsync.md)
- [WriteSPN → targeted roast](0216-ad-dacl-writespn.md)
- [AD CS ESC1 (path)](0221-ad-cs-esc1.md)