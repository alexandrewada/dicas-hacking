---
id: "0971"
categoria: "09-ad"
familia: "ad-dacl"
slug: "genericall"
angulo: "hardening"
mitre: ""
owasp: ""
tags: ["09-ad", "ad-dacl", "hardening"]
aliases: ["GenericAll em usuário/grupo", "genericall", "genericall-hardening"]
---

# GenericAll em usuário/grupo — hardening

Do PoC ao controle — GenericAll em usuário/grupo.

## Risco

BloodHound popularizou edges: GenericAll, WriteDACL, ForceChangePassword, DCSync rights,
AddMember, etc. valida o caminho em lab controlado e prova com ação mínima
(reset de conta teste, add a grupo lab), não com destruição.

## Controles desta variante

- Detalhe que pago pra ver: **Takeover direto**.

## Camadas

1) Bloqueio imediato
2) Directory Services Changes auditing; BloodHound Enterprise-like monitoring.
3) AdminSDHolder higiene; least privilege; Privileged Access Workstations;
remover ACEs excessivos.
Reteste com o mesmo PoC — critério: a prova desta variante falha.

## Exemplo

```text
checklist genericall:
- [ ] controle preventivo ativo
- [ ] telemetria cobre o PoC
- [ ] reteste com mesma prova (ad0286) falha
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

- [GenericAll em usuário/grupo](0211-ad-dacl-genericall.md)
- [GenericAll em usuário/grupo — lab](0591-ad-dacl-genericall--lab.md)
- [Direitos de DCSync](0213-ad-dacl-dcsync.md)
- [KeyCredentialLink / Shadow Credentials](0220-ad-dacl-shadowcred.md)
- [WriteSPN → targeted roast](0216-ad-dacl-writespn.md)
- [AddMember a grupo privilegiado (path)](0214-ad-dacl-addmember.md)