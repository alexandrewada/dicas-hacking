# vulnerable driver (BYOVD) — hardening

Do PoC ao controle — vulnerable driver (BYOVD).

## Risco

PrivEsc Windows combina misconfigs clássicas (unquoted service path, weak service ACL,
AlwaysInstallElevated, autologon registry) com token privileges (SeImpersonate → potato family)
e autostart extensibility. Metodologia: enum → hipótese → PoC mínimo → hardering.

## Controles desta variante

- Se não validar **Somente se ROE e lab**, a nota fica genérica.

## Camadas

1) Bloqueio imediato
2) Sysmon process creation; service changes; sticky potato patterns.
3) Least privilege services; remove SeImpersonate de app pools quando possível;
hardening LAPS; patch.
Reteste com o mesmo PoC — critério: a prova desta variante falha.

## Exemplo

```text
checklist driver:
- [ ] controle preventivo ativo
- [ ] telemetria cobre o PoC
- [ ] reteste com mesma prova (e15f01) falha
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