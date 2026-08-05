---
id: "0242"
categoria: "10-windows"
familia: "win-cred"
slug: "dpapi"
angulo: "base"
mitre: ""
owasp: ""
tags: ["10-windows", "win-cred", "base"]
aliases: ["DPAPI masterkey abuse", "dpapi"]
---

# DPAPI masterkey abuse

## Contexto

LSASS dump, DPAPI, Credential Manager, LSA secrets, certificates e browser stores
são fontes típicas pós-exploração. Em engajamentos com EDR, prefira técnicas menos ruidosas
e contas de teste; coordene dumping com o cliente.

## Detalhe

- Variante DPAPI masterkey abuse: trato separado da família `win-cred`.

## Execução

1. Verifico privilégios e políticas de credential guard.
2. Enumero stores não-LSASS primeiro (files, vault, scripts).
3. Se autorizado, avalio LSASS com método acordado.
4. Correlaciono credenciais com lateral movement.
5. Rotaciono segredos expostos após o teste.

## Exemplo

```powershell
# lab Windows — enum sem LSASS dump em prod
Get-Acl C:\ServicePath\svc.exe | Format-List
sc.exe qc SVC_dpapi
# writable + priv service = privesc path tag 861b0e
```

## OpSec

Dump de LSASS pode crashar hosts — com cautela. LSASS só em lab ou ROE explícito. Em prod prefiro DPAPI/registry com conta teste.

## Cuidados

Dump de LSASS pode crashar hosts — com cautela.
Não exfiltro NTDS sem escopo de Domain Compromise explícito.

## Fechamento

| | |
|---|---|
| Detecção | EDR LSASS access; Sysmon 10; Credential Guard. |
| Remediação | Credential Guard; LAPS; gMSA; proibir debug privileges; vault hygiene. |
| Evidência | Tipo de credencial; host; uso em lateral (sem dumps completos). |

## Refs

- [MITRE ATT&CK](https://attack.mitre.org/)
- [SpecterOps — DPAPI](https://posts.specterops.io/operational-guidance-for-offensive-user-dpapi-abuse-1fb7fac8b107)
- [MITRE ATT&CK T1003](https://attack.mitre.org/techniques/T1003/)

## Relacionadas

- [DPAPI masterkey abuse — lab](0622-win-cred-dpapi--lab.md)
- [browser saved passwords](0247-win-cred-browser.md)
- [user/machine certs](0249-win-cred-cert.md)
- [GPP/legacy secrets](0250-win-cred-gpp.md)
- [LSA secrets / autologon](0244-win-cred-lsa.md)