---
id: "0246"
categoria: "10-windows"
familia: "win-cred"
slug: "ntds"
angulo: "base"
mitre: ""
owasp: ""
tags: ["10-windows", "win-cred", "base"]
aliases: ["NTDS.dit (escopo DC)", "ntds"]
---

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

- [MITRE ATT&CK](https://attack.mitre.org/)
- [SpecterOps — DPAPI](https://posts.specterops.io/operational-guidance-for-offensive-user-dpapi-abuse-1fb7fac8b107)
- [MITRE ATT&CK T1003](https://attack.mitre.org/techniques/T1003/)

## Relacionadas

- [NTDS.dit (escopo DC) — lab](0626-win-cred-ntds--lab.md)
- [browser saved passwords](0247-win-cred-browser.md)
- [user/machine certs](0249-win-cred-cert.md)
- [DPAPI masterkey abuse](0242-win-cred-dpapi.md)
- [GPP/legacy secrets](0250-win-cred-gpp.md)