# Potato / SeImpersonate — lab

Sandbox throwaway — Potato / SeImpersonate sem ruído de cliente.

## Contexto

PrivEsc Windows combina misconfigs clássicas (unquoted service path, weak service ACL,
AlwaysInstallElevated, autologon registry) com token privileges (SeImpersonate → potato family)
e autostart extensibility. Metodologia: enum → hipótese → PoC mínimo → hardering.

## Variante

- Variante Potato family (SeImpersonate): trato separado da família `win-privesc`.

## Setup

Ativo mínimo. Duas identidades se for authz.
Restore point.

## Fluxo

1. Enumero com winPEAS/SharpUp/manual (serviços, tasks, registry).
2. Valido writability e restart conditions.
3. Exploro tokens privilegiados se presentes.
4. Provar SYSTEM com payload benigno.
5. Limpar persistência de teste.

## No lab ficou assim

```powershell
# lab Windows — enum sem LSASS dump em prod
Get-Acl C:\ServicePath\svc.exe | Format-List
sc.exe qc SVC_potato
# writable + priv service = privesc path tag 4d158c
```

## Pitfall

Cuidado com AV/EDR em produção — combine com exclusions acordadas.
Não desabilito defesas sem autorização.

DLL/serviço: path writable + binário sob identidade privilegiada. Sem os dois, não é privesc.

## Prova do lab

Vetor; whoami /priv; prova SYSTEM; cleanup.

## Refs

- PayloadsAllTheThings Windows PrivEsc
- MITRE PrivEsc