# scheduled task ACL

`T1548 Abuse Elevation Control / T1053`

## Por que importa

PrivEsc Windows combina misconfigs clássicas (unquoted service path, weak service ACL,
AlwaysInstallElevated, autologon registry) com token privileges (SeImpersonate → potato family)
e autostart extensibility. Metodologia: enum → hipótese → PoC mínimo → hardering.

## Variante

- Exporto shortest path até tier0 com o edge exato. Sem isso a remediação vira 'olha o BloodHound'.

## Passo a passo

1. Enumero com winPEAS/SharpUp/manual (serviços, tasks, registry).
2. Valido writability e restart conditions.
3. Exploro tokens privilegiados se presentes.
4. Provar SYSTEM com payload benigno.
5. Limpar persistência de teste.

## No lab ficou assim

```powershell
# lab Windows — enum sem LSASS dump em prod
Get-Acl C:\ServicePath\svc.exe | Format-List
sc.exe qc SVC_sched-task
# writable + priv service = privesc path tag 6ad8fc
```

## Nota de operador

LSASS só em lab ou ROE explícito. Em prod prefiro DPAPI/registry com conta teste.

## Armadilha

Cuidado com AV/EDR em produção — combine com exclusions acordadas.
Não desabilito defesas sem autorização.

Já abri High demais em scheduled task ACL por sintoma sem efeito. Cruzei com: Sysmon process creation; service changes; sticky potato patterns. Sem side-effect, baixo.

## Depois

Detecção — Sysmon process creation; service changes; sticky potato patterns.

Remediação — Least privilege services; remove SeImpersonate de app pools quando possível;
hardening LAPS; patch.

No PDF — Vetor; whoami /priv; prova SYSTEM; cleanup.

## Refs

- PayloadsAllTheThings Windows PrivEsc
- MITRE PrivEsc