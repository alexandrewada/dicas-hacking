---
id: "0976"
categoria: "09-ad"
familia: "ad-dacl"
slug: "writespn"
angulo: "hardening"
mitre: ""
owasp: ""
tags: ["09-ad", "ad-dacl", "hardening"]
aliases: ["WriteSPN → targeted roast", "writespn", "writespn-hardening"]
---

# WriteSPN → targeted roast — hardening

Do PoC ao controle — WriteSPN → targeted roast.

## Risco

BloodHound popularizou edges: GenericAll, WriteDACL, ForceChangePassword, DCSync rights,
AddMember, etc. valida o caminho em lab controlado e prova com ação mínima
(reset de conta teste, add a grupo lab), não com destruição.

## Controles desta variante

- Variante WriteSPN → targeted roast: trato separado da família `ad-dacl`.

## Camadas

Controle que fecha: AdminSDHolder higiene; least privilege; Privileged Access Workstations;
remover ACEs excessivos.
Sinal que deveria existir: Directory Services Changes auditing; BloodHound Enterprise-like monitoring.

## No lab ficou assim

```text
checklist writespn:
- [ ] controle preventivo ativo
- [ ] telemetria cobre o PoC
- [ ] reteste com mesma prova (610606) falha
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

- [WriteSPN → targeted roast](0216-ad-dacl-writespn.md)
- [WriteSPN → targeted roast — lab](0596-ad-dacl-writespn--lab.md)
- [GenericAll em usuário/grupo](0211-ad-dacl-genericall.md)
- [Direitos de DCSync](0213-ad-dacl-dcsync.md)
- [KeyCredentialLink / Shadow Credentials](0220-ad-dacl-shadowcred.md)
- [Kerberoasting (TGS RC4) (path)](0201-ad-kerberoast-rc4.md)