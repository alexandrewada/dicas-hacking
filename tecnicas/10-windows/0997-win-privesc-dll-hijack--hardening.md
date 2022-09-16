# DLL hijacking — hardening

Do PoC ao controle — DLL hijacking.

## Risco

PrivEsc Windows combina misconfigs clássicas (unquoted service path, weak service ACL,
AlwaysInstallElevated, autologon registry) com token privileges (SeImpersonate → potato family)
e autostart extensibility. Metodologia: enum → hipótese → PoC mínimo → hardering.

## Controles desta variante

- **Apps trusted.** Sem isso o playbook da família mente.

## Camadas

1) Bloqueio imediato
2) Sysmon process creation; service changes; sticky potato patterns.
3) Least privilege services; remove SeImpersonate de app pools quando possível;
hardening LAPS; patch.
Reteste com o mesmo PoC — critério: a prova desta variante falha.

## PoC mínimo

```text
antes: controle ausente para dll-hijack
depois: ownership check / deny default em TARGET
verificação: PoC 7f20a5 retorna 403/blocked
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