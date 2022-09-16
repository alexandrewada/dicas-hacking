# SAM local dump — lab

Sandbox throwaway — SAM local dump sem ruído de cliente.

## Contexto

LSASS dump, DPAPI, Credential Manager, LSA secrets, certificates e browser stores
são fontes típicas pós-exploração. Em engajamentos com EDR, prefira técnicas menos ruidosas
e contas de teste; coordene dumping com o cliente.

## Variante

- Detalhe que pago pra ver: **Se admin local**.

## Setup

Ativo mínimo. Duas identidades se for authz.
Restore point.

## Fluxo

1. Verifico privilégios e políticas de credential guard.
2. Enumero stores não-LSASS primeiro (files, vault, scripts).
3. Se autorizado, avalio LSASS com método acordado.
4. Correlaciono credenciais com lateral movement.
5. Rotaciono segredos expostos após o teste.

## No lab ficou assim

```powershell
# lab Windows — enum sem LSASS dump em prod
Get-Acl C:\ServicePath\svc.exe | Format-List
sc.exe qc SVC_sam
# writable + priv service = privesc path tag 239064
```

## Pitfall

Dump de LSASS pode crashar hosts — com cautela.
Não exfiltro NTDS sem escopo de Domain Compromise explícito.

LOLBin: parent-child + linha de comando que o EDR deveria ter visto.

## Prova do lab

Tipo de credencial; host; uso em lateral (sem dumps completos).

## Refs

- MITRE Credential Access
- SpecterOps DPAPI