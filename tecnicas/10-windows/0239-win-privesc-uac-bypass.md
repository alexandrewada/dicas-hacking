# UAC bypass (lab)

**Local privesc** · `T1548 Abuse Elevation Control / T1053`

## Contexto

PrivEsc Windows combina misconfigs clássicas (unquoted service path, weak service ACL,
AlwaysInstallElevated, autologon registry) com token privileges (SeImpersonate → potato family)
e autostart extensibility. Metodologia: enum → hipótese → PoC mínimo → hardering.

## O que muda aqui

- Se não validar **Documento detecção**, a nota fica genérica.

## Como testo

1. Enumero com winPEAS/SharpUp/manual (serviços, tasks, registry).
2. Valido writability e restart conditions.
3. Exploro tokens privilegiados se presentes.
4. Provar SYSTEM com payload benigno.
5. Limpar persistência de teste.

## Exemplo

```powershell
# lab Windows — enum sem LSASS dump em prod
Get-Acl C:\ServicePath\svc.exe | Format-List
sc.exe qc SVC_uac-bypass
# writable + priv service = privesc path tag c7ed23
```

## Campo

LOLBin: parent-child + linha de comando que o EDR deveria ter visto.

Já abri High demais em UAC bypass (lab) por sintoma sem efeito. Cruzei com: Sysmon process creation; service changes; sticky potato patterns. Sem side-effect, baixo.

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