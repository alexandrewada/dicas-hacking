---
id: "0250"
categoria: "10-windows"
familia: "win-cred"
slug: "gpp"
angulo: "base"
mitre: ""
owasp: ""
tags: ["10-windows", "win-cred", "base"]
aliases: ["GPP/legacy secrets", "gpp"]
---

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

- [MITRE ATT&CK](https://attack.mitre.org/)
- [SpecterOps — DPAPI](https://posts.specterops.io/operational-guidance-for-offensive-user-dpapi-abuse-1fb7fac8b107)
- [MITRE ATT&CK T1003](https://attack.mitre.org/techniques/T1003/)

## Relacionadas

- [GPP/legacy secrets — evidência](0630-win-cred-gpp--evidencia.md)
- [browser saved passwords](0247-win-cred-browser.md)
- [user/machine certs](0249-win-cred-cert.md)
- [DPAPI masterkey abuse](0242-win-cred-dpapi.md)
- [LSA secrets / autologon](0244-win-cred-lsa.md)