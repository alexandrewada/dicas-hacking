# service binary ACL fraca

**Local privesc** · `T1548 Abuse Elevation Control / T1053`

## Contexto

PrivEsc Windows combina misconfigs clássicas (unquoted service path, weak service ACL,
AlwaysInstallElevated, autologon registry) com token privileges (SeImpersonate → potato family)
e autostart extensibility. Metodologia: enum → hipótese → PoC mínimo → hardering.

## O que muda aqui

- Exporto shortest path até tier0 com o edge exato. Sem isso a remediação vira 'olha o BloodHound'.

## Como testo

1. Enumero com winPEAS/SharpUp/manual (serviços, tasks, registry).
2. Valido writability e restart conditions.
3. Exploro tokens privilegiados se presentes.
4. Provar SYSTEM com payload benigno.
5. Limpar persistência de teste.

## Sinal / query

```powershell
# lab Windows — enum sem LSASS dump em prod
Get-Acl C:\ServicePath\svc.exe | Format-List
sc.exe qc SVC_service-acl
# writable + priv service = privesc path tag 55b7f5
```

## Campo

LSASS só em lab ou ROE explícito. Em prod prefiro DPAPI/registry com conta teste.

Já abri High demais em service binary ACL fraca por sintoma sem efeito. Cruzei com: Sysmon process creation; service changes; sticky potato patterns. Sem side-effect, baixo.

## Já me queimei

Cuidado com AV/EDR em produção — combine com exclusions acordadas.
Não desabilito defesas sem autorização.

## Blue

- Detectar: Sysmon process creation; service changes; sticky potato patterns.
- Fechar: Least privilege services; remove SeImpersonate de app pools quando possível;
hardening LAPS; patch.

## Evidência

Vetor; whoami /priv; prova SYSTEM; cleanup.

## Refs

- PayloadsAllTheThings Windows PrivEsc
- MITRE PrivEsc