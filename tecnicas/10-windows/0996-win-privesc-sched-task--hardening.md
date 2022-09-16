# scheduled task ACL — hardening

Do PoC ao controle — scheduled task ACL.

## Risco

PrivEsc Windows combina misconfigs clássicas (unquoted service path, weak service ACL,
AlwaysInstallElevated, autologon registry) com token privileges (SeImpersonate → potato family)
e autostart extensibility. Metodologia: enum → hipótese → PoC mínimo → hardering.

## Controles desta variante

- Exporto shortest path até tier0 com o edge exato. Sem isso a remediação vira 'olha o BloodHound'.

## Camadas

Hotfix: quebra a exploração direta de scheduled task ACL.
Detectivo: Sysmon process creation; service changes; sticky potato patterns.
Estrutural: Least privilege services; remove SeImpersonate de app pools quando possível;
hardening LAPS; patch.

## Exemplo

```text
antes: controle ausente para sched-task
depois: ownership check / deny default em TARGET
verificação: PoC ecd9f1 retorna 403/blocked
reteste USER_A vs USER_B
```

## Armadilha

Cuidado com AV/EDR em produção — combine com exclusions acordadas.
Não desabilito defesas sem autorização.

## Antes/depois

Vetor; whoami /priv; prova SYSTEM; cleanup.

Aceite de risco só por escrito, com prazo.

## Refs

- PayloadsAllTheThings Windows PrivEsc
- MITRE PrivEsc