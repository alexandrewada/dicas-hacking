# autologon registry secrets — lab

Critério: outro analista fecha sozinho com esta nota.

## Contexto

PrivEsc Windows combina misconfigs clássicas (unquoted service path, weak service ACL,
AlwaysInstallElevated, autologon registry) com token privileges (SeImpersonate → potato family)
e autostart extensibility. Metodologia: enum → hipótese → PoC mínimo → hardering.

## Variante

- Variante autologon registry secrets: trato separado da família `win-privesc`.

## Setup

Espelho do alvo. Sem WAF/EDR às vezes — anoto o delta.

## Fluxo

1. Enumero com winPEAS/SharpUp/manual (serviços, tasks, registry).
2. Valido writability e restart conditions.
3. Exploro tokens privilegiados se presentes.
4. Provar SYSTEM com payload benigno.
5. Limpar persistência de teste.

## Exemplo

```powershell
# lab Windows — enum sem LSASS dump em prod
Get-Acl C:\ServicePath\svc.exe | Format-List
sc.exe qc SVC_autologon
# writable + priv service = privesc path tag ab2318
```

## Pitfall

Cuidado com AV/EDR em produção — combine com exclusions acordadas.
Não desabilito defesas sem autorização.

LOLBin: parent-child + linha de comando que o EDR deveria ter visto.

## Prova do lab

Vetor; whoami /priv; prova SYSTEM; cleanup.

## Refs

- PayloadsAllTheThings Windows PrivEsc
- MITRE PrivEsc