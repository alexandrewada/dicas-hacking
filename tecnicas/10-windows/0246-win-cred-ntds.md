# NTDS.dit (escopo DC)

## Leitura rápida

LSASS dump, DPAPI, Credential Manager, LSA secrets, certificates e browser stores
são fontes típicas pós-exploração. Em engajamentos com EDR, prefira técnicas menos ruidosas
e contas de teste; coordene dumping com o cliente.

## Foco

- Detalhe que pago pra ver: **Critical path**.

## Mãos na massa

1. Verifico privilégios e políticas de credential guard.
2. Enumero stores não-LSASS primeiro (files, vault, scripts).
3. Se autorizado, avalio LSASS com método acordado.
4. Correlaciono credenciais com lateral movement.
5. Rotaciono segredos expostos após o teste.

## No lab ficou assim

```powershell
# lab Windows — enum sem LSASS dump em prod
Get-Acl C:\ServicePath\svc.exe | Format-List
sc.exe qc SVC_ntds
# writable + priv service = privesc path tag af9f0f
```

LOLBin: parent-child + linha de comando que o EDR deveria ter visto.

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