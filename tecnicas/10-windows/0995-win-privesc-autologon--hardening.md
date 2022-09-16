# autologon registry secrets — hardening

Do PoC ao controle — autologon registry secrets.

## Risco

PrivEsc Windows combina misconfigs clássicas (unquoted service path, weak service ACL,
AlwaysInstallElevated, autologon registry) com token privileges (SeImpersonate → potato family)
e autostart extensibility. Metodologia: enum → hipótese → PoC mínimo → hardering.

## Controles desta variante

- Variante autologon registry secrets: trato separado da família `win-privesc`.

## Camadas

Controle que fecha: Least privilege services; remove SeImpersonate de app pools quando possível;
hardening LAPS; patch.
Sinal que deveria existir: Sysmon process creation; service changes; sticky potato patterns.

## PoC mínimo

```text
checklist autologon:
- [ ] controle preventivo ativo
- [ ] telemetria cobre o PoC
- [ ] reteste com mesma prova (7bf02d) falha
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