---
id: "0975"
categoria: "09-ad"
familia: "ad-dacl"
slug: "forcechange"
angulo: "hardening"
mitre: "T1003"
owasp: ""
tags: ["09-ad", "ad-dacl", "hardening", "t1003"]
aliases: ["ForceChangePassword", "forcechange", "forcechange-hardening"]
---

# ForceChangePassword — hardening

Do PoC ao controle — ForceChangePassword.

## Risco

BloodHound popularizou edges: GenericAll, WriteDACL, ForceChangePassword, DCSync rights,
AddMember, etc. valida o caminho em lab controlado e prova com ação mínima
(reset de conta teste, add a grupo lab), não com destruição.

## Controles desta variante

- **Helpdesk abuse** — muda ruído e o que entra no PDF.

## Camadas

1) Bloqueio imediato
2) Directory Services Changes auditing; BloodHound Enterprise-like monitoring.
3) AdminSDHolder higiene; least privilege; Privileged Access Workstations;
remover ACEs excessivos.
Reteste com o mesmo PoC — critério: a prova desta variante falha.

## Exemplo

```text
checklist forcechange:
- [ ] controle preventivo ativo
- [ ] telemetria cobre o PoC
- [ ] reteste com mesma prova (2621be) falha
```

## Armadilha

DCSync em produção é sensível — alinhe com cliente.
Evito resetar senhas de usuários reais.

## Antes/depois

Edge BloodHound; PoC controlado; ACE dump.

Aceite de risco só por escrito, com prazo.

## Refs

- [MITRE ATT&CK T1003](https://attack.mitre.org/techniques/T1003/)
- [MITRE ATT&CK T1484](https://attack.mitre.org/techniques/T1484/)
- [SpecterOps — BloodHound docs](https://bloodhound.specterops.io/)
- [MITRE ATT&CK](https://attack.mitre.org/)

## Relacionadas

- [ForceChangePassword](0215-ad-dacl-forcechange.md)
- [ForceChangePassword — lab](0595-ad-dacl-forcechange--lab.md)
- [GenericAll em usuário/grupo](0211-ad-dacl-genericall.md)
- [Direitos de DCSync](0213-ad-dacl-dcsync.md)
- [KeyCredentialLink / Shadow Credentials](0220-ad-dacl-shadowcred.md)
- [WriteSPN → targeted roast](0216-ad-dacl-writespn.md)