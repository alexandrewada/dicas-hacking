# unquoted service path — hardening

Do PoC ao controle — unquoted service path.

## Risco

PrivEsc Windows combina misconfigs clássicas (unquoted service path, weak service ACL,
AlwaysInstallElevated, autologon registry) com token privileges (SeImpersonate → potato family)
e autostart extensibility. Metodologia: enum → hipótese → PoC mínimo → hardering.

## Controles desta variante

- Variante unquoted service path: trato separado da família `win-privesc`.

## Camadas

1) Bloqueio imediato
2) Sysmon process creation; service changes; sticky potato patterns.
3) Least privilege services; remove SeImpersonate de app pools quando possível;
hardening LAPS; patch.
Reteste com o mesmo PoC — critério: a prova desta variante falha.

## No lab ficou assim

```bash
# verificação pós-hardening unquoted
curl -sk -o /dev/null -w '%{http_code}\n' https://app.lab.local/unquoted/usr_01HZX \
  -H 'Cookie: session=USER_B'
# esperado 403 — tag ee20c5
```

## Armadilha

Cuidado com AV/EDR em produção — combine com exclusions acordadas.
Não desabilito defesas sem autorização.

## Antes/depois

Vetor; whoami /priv; prova SYSTEM; cleanup.

Aceite de risco só por escrito, com prazo.

## Refs

- PayloadsAllTheThings Windows PrivEsc
- MITRE PrivEsc