# autologon registry secrets

## Contexto

PrivEsc Windows combina misconfigs clássicas (unquoted service path, weak service ACL,
AlwaysInstallElevated, autologon registry) com token privileges (SeImpersonate → potato family)
e autostart extensibility. Metodologia: enum → hipótese → PoC mínimo → hardering.

## Detalhe

- Variante autologon registry secrets: trato separado da família `win-privesc`.

## Execução

1. Enumero com winPEAS/SharpUp/manual (serviços, tasks, registry).
2. Valido writability e restart conditions.
3. Exploro tokens privilegiados se presentes.
4. Provar SYSTEM com payload benigno.
5. Limpar persistência de teste.

## Sinal / query

```powershell
# lab Windows — enum sem LSASS dump em prod
Get-Acl C:\ServicePath\svc.exe | Format-List
sc.exe qc SVC_autologon
# writable + priv service = privesc path tag ba573d
```

## OpSec

LOLBin: parent-child + linha de comando que o EDR deveria ter visto.

## Cuidados

Cuidado com AV/EDR em produção — combine com exclusions acordadas.
Não desabilito defesas sem autorização.

## Fechamento

| | |
|---|---|
| Detecção | Sysmon process creation; service changes; sticky potato patterns. |
| Remediação | Least privilege services; remove SeImpersonate de app pools quando possível;
hardening LAPS; patch. |
| Evidência | Vetor; whoami /priv; prova SYSTEM; cleanup. |

## Refs

- PayloadsAllTheThings Windows PrivEsc
- MITRE PrivEsc