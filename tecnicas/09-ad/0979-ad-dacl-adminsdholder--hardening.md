---
id: "0979"
categoria: "09-ad"
familia: "ad-dacl"
slug: "adminsdholder"
angulo: "hardening"
mitre: ""
owasp: ""
tags: ["09-ad", "ad-dacl", "hardening"]
aliases: ["AdminSDHolder backdoor", "adminsdholder", "adminsdholder-hardening"]
---

# AdminSDHolder backdoor — hardening

Do PoC ao controle — AdminSDHolder backdoor.

## Risco

BloodHound popularizou edges: GenericAll, WriteDACL, ForceChangePassword, DCSync rights,
AddMember, etc. valida o caminho em lab controlado e prova com ação mínima
(reset de conta teste, add a grupo lab), não com destruição.

## Controles desta variante

- Detalhe que pago pra ver: **Persistência**.

## Camadas

Hotfix: quebra a exploração direta de AdminSDHolder backdoor.
Detectivo: Directory Services Changes auditing; BloodHound Enterprise-like monitoring.
Estrutural: AdminSDHolder higiene; least privilege; Privileged Access Workstations;
remover ACEs excessivos.

## Exemplo

```text
antes: controle ausente para adminsdholder
depois: ownership check / deny default em TARGET
verificação: PoC 164a0c retorna 403/blocked
reteste USER_A vs USER_B
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
- [MITRE ATT&CK T1484](https://attack.mitre.org/techniques/T1484/)

## Relacionadas

- [AdminSDHolder backdoor](0219-ad-dacl-adminsdholder.md)
- [AdminSDHolder backdoor — lab](0599-ad-dacl-adminsdholder--lab.md)
- [GenericAll em usuário/grupo](0211-ad-dacl-genericall.md)
- [Direitos de DCSync](0213-ad-dacl-dcsync.md)
- [KeyCredentialLink / Shadow Credentials](0220-ad-dacl-shadowcred.md)
- [WriteSPN → targeted roast](0216-ad-dacl-writespn.md)