# vulnerable driver (BYOVD) — lab

Critério: outro analista fecha sozinho com esta nota.

## Contexto

PrivEsc Windows combina misconfigs clássicas (unquoted service path, weak service ACL,
AlwaysInstallElevated, autologon registry) com token privileges (SeImpersonate → potato family)
e autostart extensibility. Metodologia: enum → hipótese → PoC mínimo → hardering.

## Variante

- Se não validar **Somente se ROE e lab**, a nota fica genérica.

## Setup

Espelho do alvo. Sem WAF/EDR às vezes — anoto o delta.

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
sc.exe qc SVC_driver
# writable + priv service = privesc path tag 995cd5
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