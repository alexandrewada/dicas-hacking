---
id: "0980"
categoria: "09-ad"
familia: "ad-dacl"
slug: "shadowcred"
angulo: "hardening"
mitre: ""
owasp: ""
tags: ["09-ad", "ad-dacl", "hardening"]
aliases: ["KeyCredentialLink / Shadow Credentials", "shadowcred", "shadowcred-hardening"]
---

# KeyCredentialLink / Shadow Credentials — hardening

Do PoC ao controle — KeyCredentialLink / Shadow Credentials.

## Risco

BloodHound popularizou edges: GenericAll, WriteDACL, ForceChangePassword, DCSync rights,
AddMember, etc. valida o caminho em lab controlado e prova com ação mínima
(reset de conta teste, add a grupo lab), não com destruição.

## Controles desta variante

- **PKINIT abuse** — muda ruído e o que entra no PDF.

## Camadas

Controle que fecha: AdminSDHolder higiene; least privilege; Privileged Access Workstations;
remover ACEs excessivos.
Sinal que deveria existir: Directory Services Changes auditing; BloodHound Enterprise-like monitoring.

## No lab ficou assim

```text
antes: controle ausente para shadowcred
depois: ownership check / deny default em TARGET
verificação: PoC 5ca9c4 retorna 403/blocked
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

- [KeyCredentialLink / Shadow Credentials](0220-ad-dacl-shadowcred.md)
- [KeyCredentialLink / Shadow Credentials — lab](0600-ad-dacl-shadowcred--lab.md)
- [GenericAll em usuário/grupo](0211-ad-dacl-genericall.md)
- [Direitos de DCSync](0213-ad-dacl-dcsync.md)
- [WriteSPN → targeted roast](0216-ad-dacl-writespn.md)
- [AD CS ESC1 (path)](0221-ad-cs-esc1.md)