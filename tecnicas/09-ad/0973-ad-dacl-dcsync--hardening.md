---
id: "0973"
categoria: "09-ad"
familia: "ad-dacl"
slug: "dcsync"
angulo: "hardening"
mitre: ""
owasp: ""
tags: ["09-ad", "ad-dacl", "hardening"]
aliases: ["Direitos de DCSync", "dcsync", "dcsync-hardening"]
---

# Direitos de DCSync — hardening

Do PoC ao controle — Direitos de DCSync.

## Risco

BloodHound popularizou edges: GenericAll, WriteDACL, ForceChangePassword, DCSync rights,
AddMember, etc. valida o caminho em lab controlado e prova com ação mínima
(reset de conta teste, add a grupo lab), não com destruição.

## Controles desta variante

- Se não validar **Credential dump path**, a nota fica genérica.
- GetChanges/GetChangesAll em conta que não deveria ter — não em DA óbvio.

## Camadas

Hotfix: quebra a exploração direta de Direitos de DCSync.
Detectivo: Directory Services Changes auditing; BloodHound Enterprise-like monitoring.
Estrutural: AdminSDHolder higiene; least privilege; Privileged Access Workstations;
remover ACEs excessivos.

## PoC mínimo

```text
checklist dcsync:
- [ ] controle preventivo ativo
- [ ] telemetria cobre o PoC
- [ ] reteste com mesma prova (7548c0) falha
```

## Armadilha

DCSync em produção é sensível — alinhe com cliente.
Evito resetar senhas de usuários reais.

## Antes/depois

Edge BloodHound; PoC controlado; ACE dump.

Aceite de risco só por escrito, com prazo.

## Refs

- [SpecterOps — BloodHound docs](https://bloodhound.specterops.io/)
- [MITRE ATT&CK](https://attack.mitre.org/)
- [MITRE ATT&CK T1003.006](https://attack.mitre.org/techniques/T1003/006/)
- [MITRE ATT&CK T1484](https://attack.mitre.org/techniques/T1484/)

## Relacionadas

- [Direitos de DCSync](0213-ad-dacl-dcsync.md)
- [Direitos de DCSync — lab](0593-ad-dacl-dcsync--lab.md)
- [GenericAll em usuário/grupo](0211-ad-dacl-genericall.md)
- [KeyCredentialLink / Shadow Credentials](0220-ad-dacl-shadowcred.md)
- [WriteSPN → targeted roast](0216-ad-dacl-writespn.md)
- [AD CS ESC1 (path)](0221-ad-cs-esc1.md)
- [NTDS.dit (escopo DC) (path)](../10-windows/0246-win-cred-ntds.md)