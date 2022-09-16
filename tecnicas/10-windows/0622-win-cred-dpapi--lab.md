# DPAPI masterkey abuse — lab

Sandbox throwaway — DPAPI masterkey abuse sem ruído de cliente.

## Contexto

LSASS dump, DPAPI, Credential Manager, LSA secrets, certificates e browser stores
são fontes típicas pós-exploração. Em engajamentos com EDR, prefira técnicas menos ruidosas
e contas de teste; coordene dumping com o cliente.

## Variante

- Variante DPAPI masterkey abuse: trato separado da família `win-cred`.

## Setup

Ativo mínimo. Duas identidades se for authz.
Restore point.

## Fluxo

1. Verifico privilégios e políticas de credential guard.
2. Enumero stores não-LSASS primeiro (files, vault, scripts).
3. Se autorizado, avalio LSASS com método acordado.
4. Correlaciono credenciais com lateral movement.
5. Rotaciono segredos expostos após o teste.

## Sinal / query

```powershell
# lab Windows — enum sem LSASS dump em prod
Get-Acl C:\ServicePath\svc.exe | Format-List
sc.exe qc SVC_dpapi
# writable + priv service = privesc path tag 9c4cf3
```

## Pitfall

Dump de LSASS pode crashar hosts — com cautela.
Não exfiltro NTDS sem escopo de Domain Compromise explícito.

LSASS só em lab ou ROE explícito. Em prod prefiro DPAPI/registry com conta teste.

## Prova do lab

Tipo de credencial; host; uso em lateral (sem dumps completos).

## Refs

- MITRE Credential Access
- SpecterOps DPAPI