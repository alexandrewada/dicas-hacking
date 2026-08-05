---
id: "0591"
categoria: "09-ad"
familia: "ad-dacl"
slug: "genericall"
angulo: "lab"
mitre: ""
owasp: ""
tags: ["09-ad", "ad-dacl", "lab"]
aliases: ["GenericAll em usuário/grupo", "genericall", "genericall-lab"]
---

# GenericAll em usuário/grupo — lab

Lab só pra GenericAll em usuário/grupo. Se não reproduz isolado, não confio no finding de prod.

## Contexto

BloodHound popularizou edges: GenericAll, WriteDACL, ForceChangePassword, DCSync rights,
AddMember, etc. valida o caminho em lab controlado e prova com ação mínima
(reset de conta teste, add a grupo lab), não com destruição.

## Variante

- Detalhe que pago pra ver: **Takeover direto**.

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

## No lab ficou assim

```bash
# DACL genericall — prova de ACE sem mudança destrutiva
bloodyAD --host DC01.lab.local -d lab.local -u USER_A -p PASS_LAB \
  get object 'CN=TARGET_OBJ,OU=Lab,DC=lab,DC=local' --attr nTSecurityDescriptor
# edge esperado: genericall → conta teste; tag bddbb8
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

- [GenericAll em usuário/grupo](0211-ad-dacl-genericall.md)
- [GenericAll em usuário/grupo — hardening](0971-ad-dacl-genericall--hardening.md)
- [Direitos de DCSync](0213-ad-dacl-dcsync.md)
- [KeyCredentialLink / Shadow Credentials](0220-ad-dacl-shadowcred.md)
- [WriteSPN → targeted roast](0216-ad-dacl-writespn.md)
- [AddMember a grupo privilegiado (path)](0214-ad-dacl-addmember.md)