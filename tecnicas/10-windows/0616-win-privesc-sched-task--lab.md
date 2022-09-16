# scheduled task ACL — lab

Lab só pra scheduled task ACL. Se não reproduz isolado, não confio no finding de prod.

## Contexto

PrivEsc Windows combina misconfigs clássicas (unquoted service path, weak service ACL,
AlwaysInstallElevated, autologon registry) com token privileges (SeImpersonate → potato family)
e autostart extensibility. Metodologia: enum → hipótese → PoC mínimo → hardering.

## Variante

- Exporto shortest path até tier0 com o edge exato. Sem isso a remediação vira 'olha o BloodHound'.

## Setup

VM/conta throwaway na versão parecida.
Snapshot antes.
Cleanup escrito antes de explorar.

## Fluxo

1. Enumero com winPEAS/SharpUp/manual (serviços, tasks, registry).
2. Valido writability e restart conditions.
3. Exploro tokens privilegiados se presentes.
4. Provar SYSTEM com payload benigno.
5. Limpar persistência de teste.

## PoC mínimo

```powershell
# lab Windows — enum sem LSASS dump em prod
Get-Acl C:\ServicePath\svc.exe | Format-List
sc.exe qc SVC_sched-task
# writable + priv service = privesc path tag 67d7e4
```

## Pitfall

Cuidado com AV/EDR em produção — combine com exclusions acordadas.
Não desabilito defesas sem autorização.

LSASS só em lab ou ROE explícito. Em prod prefiro DPAPI/registry com conta teste.

## Prova do lab

Vetor; whoami /priv; prova SYSTEM; cleanup.

## Refs

- PayloadsAllTheThings Windows PrivEsc
- MITRE PrivEsc