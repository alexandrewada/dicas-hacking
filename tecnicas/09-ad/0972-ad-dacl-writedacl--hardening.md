---
id: "0972"
categoria: "09-ad"
familia: "ad-dacl"
slug: "writedacl"
angulo: "hardening"
mitre: ""
owasp: ""
tags: ["09-ad", "ad-dacl", "hardening"]
aliases: ["WriteDACL → escalate ACE", "writedacl", "writedacl-hardening"]
---

# WriteDACL → escalate ACE — hardening

Do PoC ao controle — WriteDACL → escalate ACE.

## Risco

BloodHound popularizou edges: GenericAll, WriteDACL, ForceChangePassword, DCSync rights,
AddMember, etc. valida o caminho em lab controlado e prova com ação mínima
(reset de conta teste, add a grupo lab), não com destruição.

## Controles desta variante

- Se não validar **Self-grant**, a nota fica genérica.
- Exporto shortest path até tier0 com o edge exato. Sem isso a remediação vira 'olha o BloodHound'.

## Camadas

Hotfix: quebra a exploração direta de WriteDACL → escalate ACE.
Detectivo: Directory Services Changes auditing; BloodHound Enterprise-like monitoring.
Estrutural: AdminSDHolder higiene; least privilege; Privileged Access Workstations;
remover ACEs excessivos.

## Exemplo

```bash
# verificação pós-hardening writedacl
curl -sk -o /dev/null -w '%{http_code}\n' https://app.lab.local/writedacl/usr_01HZX \
  -H 'Cookie: session=USER_B'
# esperado 403 — tag b90128
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

- [WriteDACL → escalate ACE](0212-ad-dacl-writedacl.md)
- [WriteDACL → escalate ACE — lab](0592-ad-dacl-writedacl--lab.md)
- [GenericAll em usuário/grupo](0211-ad-dacl-genericall.md)
- [Direitos de DCSync](0213-ad-dacl-dcsync.md)
- [KeyCredentialLink / Shadow Credentials](0220-ad-dacl-shadowcred.md)
- [WriteSPN → targeted roast](0216-ad-dacl-writespn.md)