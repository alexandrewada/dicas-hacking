# token duplication

**Local privesc** · `T1548 Abuse Elevation Control / T1053`

PrivEsc Windows combina misconfigs clássicas (unquoted service path, weak service ACL,
AlwaysInstallElevated, autologon registry) com token privileges (SeImpersonate → potato family)
e autostart extensibility. Metodologia: enum → hipótese → PoC mínimo → hardering.

**Variante:** Variante token duplication: trato separado da família `win-privesc`.

**Método**

1. Enumero com winPEAS/SharpUp/manual (serviços, tasks, registry).
2. Valido writability e restart conditions.
3. Exploro tokens privilegiados se presentes.
4. Provar SYSTEM com payload benigno.
5. Limpar persistência de teste.

## Sinal / query

```powershell
# lab Windows — enum sem LSASS dump em prod
Get-Acl C:\ServicePath\svc.exe | Format-List
sc.exe qc SVC_token-dup
# writable + priv service = privesc path tag bcb499
```

**Freio:** Cuidado com AV/EDR em produção — combine com exclusions acordadas.

token duplication: se não reproduz efeito (authz/dado/exec), não infla severidade. Referência de sinal: Sysmon process creation; service changes; sticky potato patterns.

Detecto via: Sysmon process creation; service changes; sticky potato patterns.

Corrijo com: Least privilege services; remove SeImpersonate de app pools quando possível;
hardening LAPS; patch.

Levo no report: Vetor; whoami /priv; prova SYSTEM; cleanup.

Refs: PayloadsAllTheThings Windows PrivEsc, MITRE PrivEsc