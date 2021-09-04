# controle de OU — hardening

Do PoC ao controle — controle de OU.

## Risco

BloodHound popularizou edges: GenericAll, WriteDACL, ForceChangePassword, DCSync rights,
AddMember, etc. valida o caminho em lab controlado e prova com ação mínima
(reset de conta teste, add a grupo lab), não com destruição.

## Controles desta variante

- Detalhe que pago pra ver: **Descendant abuse**.

## Camadas

Hotfix: quebra a exploração direta de controle de OU.
Detectivo: Directory Services Changes auditing; BloodHound Enterprise-like monitoring.
Estrutural: AdminSDHolder higiene; least privilege; Privileged Access Workstations;
remover ACEs excessivos.

## PoC mínimo

```text
antes: controle ausente para ou
depois: ownership check / deny default em TARGET
verificação: PoC 08255c retorna 403/blocked
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