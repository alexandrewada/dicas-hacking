---
id: "0593"
categoria: "09-ad"
familia: "ad-dacl"
slug: "dcsync"
angulo: "lab"
mitre: ""
owasp: ""
tags: ["09-ad", "ad-dacl", "lab"]
aliases: ["Direitos de DCSync", "dcsync", "dcsync-lab"]
---

# Direitos de DCSync — lab

Sandbox throwaway — Direitos de DCSync sem ruído de cliente.

## Contexto

BloodHound popularizou edges: GenericAll, WriteDACL, ForceChangePassword, DCSync rights,
AddMember, etc. valida o caminho em lab controlado e prova com ação mínima
(reset de conta teste, add a grupo lab), não com destruição.

## Variante

- Se não validar **Credential dump path**, a nota fica genérica.
- GetChanges/GetChangesAll em conta que não deveria ter — não em DA óbvio.

## Setup

Ativo mínimo. Duas identidades se for authz.
Restore point.

## Fluxo

1. Coleto dados BloodHound com credencial autorizada.
2. Analisar paths até Dualidade DA/Tier0.
3. Valido ACEs exploráveis com ação mínima.
4. Documento objeto, ACE e impacto.
5. Propor remediação (remove ACE, tiering).

## Exemplo

```bash
# DACL dcsync — prova de ACE sem mudança destrutiva
bloodyAD --host DC01.lab.local -d lab.local -u USER_A -p PASS_LAB \
  get object 'CN=TARGET_OBJ,OU=Lab,DC=lab,DC=local' --attr nTSecurityDescriptor
# edge esperado: dcsync → conta teste; tag d95ae8
```

## Pitfall

DCSync em produção é sensível — alinhe com cliente.
Evito resetar senhas de usuários reais.

Ritmo no KDC/LDAP. Conta low-priv. Zero mudança destrutiva em objeto prod sem janela.

## Prova do lab

Edge BloodHound; PoC controlado; ACE dump.

## Refs

- [SpecterOps — BloodHound docs](https://bloodhound.specterops.io/)
- [MITRE ATT&CK](https://attack.mitre.org/)
- [MITRE ATT&CK T1003.006](https://attack.mitre.org/techniques/T1003/006/)
- [MITRE ATT&CK T1484](https://attack.mitre.org/techniques/T1484/)

## Relacionadas

- [Direitos de DCSync](0213-ad-dacl-dcsync.md)
- [Direitos de DCSync — hardening](0973-ad-dacl-dcsync--hardening.md)
- [GenericAll em usuário/grupo](0211-ad-dacl-genericall.md)
- [KeyCredentialLink / Shadow Credentials](0220-ad-dacl-shadowcred.md)
- [WriteSPN → targeted roast](0216-ad-dacl-writespn.md)
- [AD CS ESC1 (path)](0221-ad-cs-esc1.md)
- [NTDS.dit (escopo DC) (path)](../10-windows/0246-win-cred-ntds.md)