# AddMember a grupo privilegiado — hardening

Do PoC ao controle — AddMember a grupo privilegiado.

## Risco

BloodHound popularizou edges: GenericAll, WriteDACL, ForceChangePassword, DCSync rights,
AddMember, etc. valida o caminho em lab controlado e prova com ação mínima
(reset de conta teste, add a grupo lab), não com destruição.

## Controles desta variante

- Variante AddMember a grupo privilegiado: trato separado da família `ad-dacl`.

## Camadas

1) Bloqueio imediato
2) Directory Services Changes auditing; BloodHound Enterprise-like monitoring.
3) AdminSDHolder higiene; least privilege; Privileged Access Workstations;
remover ACEs excessivos.
Reteste com o mesmo PoC — critério: a prova desta variante falha.

## No lab ficou assim

```text
antes: controle ausente para addmember
depois: ownership check / deny default em TARGET
verificação: PoC 770fa5 retorna 403/blocked
reteste USER_A vs USER_B
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