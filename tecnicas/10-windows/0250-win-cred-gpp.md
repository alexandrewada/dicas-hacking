# GPP/legacy secrets

## Leitura rápida

LSASS dump, DPAPI, Credential Manager, LSA secrets, certificates e browser stores
são fontes típicas pós-exploração. Em engajamentos com EDR, prefira técnicas menos ruidosas
e contas de teste; coordene dumping com o cliente.

## Foco

- Variante GPP/legacy secrets: trato separado da família `win-cred`.

## Mãos na massa

1. Verifico privilégios e políticas de credential guard.
2. Enumero stores não-LSASS primeiro (files, vault, scripts).
3. Se autorizado, avalio LSASS com método acordado.
4. Correlaciono credenciais com lateral movement.
5. Rotaciono segredos expostos após o teste.

## PoC mínimo

```powershell
# lab Windows — enum sem LSASS dump em prod
Get-Acl C:\ServicePath\svc.exe | Format-List
sc.exe qc SVC_gpp
# writable + priv service = privesc path tag 91ff42
```

LSASS só em lab ou ROE explícito. Em prod prefiro DPAPI/registry com conta teste.

## Pitfall

Dump de LSASS pode crashar hosts — com cautela.
Não exfiltro NTDS sem escopo de Domain Compromise explícito.

## Detecção / remediação

EDR LSASS access; Sysmon 10; Credential Guard.

→ Credential Guard; LAPS; gMSA; proibir debug privileges; vault hygiene.

## Prova

Tipo de credencial; host; uso em lateral (sem dumps completos).

## Refs

- MITRE Credential Access
- SpecterOps DPAPI