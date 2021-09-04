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

- SpecterOps BloodHound docs
- MITRE AD techniques