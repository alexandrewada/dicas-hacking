# vulnerable driver (BYOVD)

**Local privesc** · `T1548 Abuse Elevation Control / T1053`

## Contexto

PrivEsc Windows combina misconfigs clássicas (unquoted service path, weak service ACL,
AlwaysInstallElevated, autologon registry) com token privileges (SeImpersonate → potato family)
e autostart extensibility. Metodologia: enum → hipótese → PoC mínimo → hardering.

## Como eu faço

1. Enumero com winPEAS/SharpUp/manual (serviços, tasks, registry).
2. Valido writability e restart conditions.
3. Exploro tokens privilegiados se presentes.
4. Provar SYSTEM com payload benigno.
5. Limpar persistência de teste.

## PoC mínimo

```powershell
# lab Windows — enum sem LSASS dump em prod
Get-Acl C:\ServicePath\svc.exe | Format-List
sc.exe qc SVC_driver
# writable + priv service = privesc path tag 3ed031
```

## Diferencial desta nota

- Se não validar **Somente se ROE e lab**, a nota fica genérica.

Antes de Critical em vulnerable driver (BYOVD), confiro se a telemetria que eu cobraria reagiria — Sysmon process creation; service changes; sticky potato patterns.

## Onde já errei

Cuidado com AV/EDR em produção — combine com exclusions acordadas.
Não desabilito defesas sem autorização.

DLL/serviço: path writable + binário sob identidade privilegiada. Sem os dois, não é privesc.

## Entrega

- blue: Sysmon process creation; service changes; sticky potato patterns.
- fix: Least privilege services; remove SeImpersonate de app pools quando possível;
hardening LAPS; patch.
- proof: Vetor; whoami /priv; prova SYSTEM; cleanup.

## Refs

- PayloadsAllTheThings Windows PrivEsc
- MITRE PrivEsc