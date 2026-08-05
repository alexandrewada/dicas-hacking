---
id: "0214"
categoria: "09-ad"
familia: "ad-dacl"
slug: "addmember"
angulo: "base"
mitre: "T1003"
owasp: ""
tags: ["09-ad", "ad-dacl", "base", "t1003"]
aliases: ["AddMember a grupo privilegiado", "addmember"]
---

# AddMember a grupo privilegiado

**Identity** · `T1003 / T1484 (adjacente) / AbuseACE`

## Contexto

BloodHound popularizou edges: GenericAll, WriteDACL, ForceChangePassword, DCSync rights,
AddMember, etc. valida o caminho em lab controlado e prova com ação mínima
(reset de conta teste, add a grupo lab), não com destruição.

## Como eu faço

1. Coleto dados BloodHound com credencial autorizada.
2. Analisar paths até Dualidade DA/Tier0.
3. Valido ACEs exploráveis com ação mínima.
4. Documento objeto, ACE e impacto.
5. Propor remediação (remove ACE, tiering).

## PoC mínimo

```bash
# DACL addmember — prova de ACE sem mudança destrutiva
bloodyAD --host DC01.lab.local -d lab.local -u USER_A -p PASS_LAB \
  get object 'CN=TARGET_OBJ,OU=Lab,DC=lab,DC=local' --attr nTSecurityDescriptor
# edge esperado: addmember → conta teste; tag 0df362
```

## Diferencial desta nota

- Variante AddMember a grupo privilegiado: trato separado da família `ad-dacl`.

Falso amigo em AddMember a grupo privilegiado: UI/log gritam, impacto não. Exijo Directory Services Changes auditing.

## Onde já errei

DCSync em produção é sensível — alinhe com cliente.
Evito resetar senhas de usuários reais.

Ritmo no KDC/LDAP. Conta low-priv. Zero mudança destrutiva em objeto prod sem janela.

## Entrega

- blue: Directory Services Changes auditing; BloodHound Enterprise-like monitoring.
- fix: AdminSDHolder higiene; least privilege; Privileged Access Workstations;
remover ACEs excessivos.
- proof: Edge BloodHound; PoC controlado; ACE dump.

## Refs

- [MITRE ATT&CK T1003](https://attack.mitre.org/techniques/T1003/)
- [MITRE ATT&CK T1484](https://attack.mitre.org/techniques/T1484/)
- [SpecterOps — BloodHound docs](https://bloodhound.specterops.io/)
- [MITRE ATT&CK](https://attack.mitre.org/)

## Relacionadas

- [AddMember a grupo privilegiado — lab](0594-ad-dacl-addmember--lab.md)
- [AddMember a grupo privilegiado — hardening](0974-ad-dacl-addmember--hardening.md)
- [GenericAll em usuário/grupo](0211-ad-dacl-genericall.md)
- [Direitos de DCSync](0213-ad-dacl-dcsync.md)
- [KeyCredentialLink / Shadow Credentials](0220-ad-dacl-shadowcred.md)
- [WriteSPN → targeted roast](0216-ad-dacl-writespn.md)