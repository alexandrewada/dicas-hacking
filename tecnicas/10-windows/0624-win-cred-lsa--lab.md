---
id: "0624"
categoria: "10-windows"
familia: "win-cred"
slug: "lsa"
angulo: "lab"
mitre: ""
owasp: ""
tags: ["10-windows", "win-cred", "lab"]
aliases: ["LSA secrets / autologon", "lsa", "lsa-lab"]
---

# LSA secrets / autologon — lab

Critério: outro analista fecha sozinho com esta nota.

## Contexto

LSASS dump, DPAPI, Credential Manager, LSA secrets, certificates e browser stores
são fontes típicas pós-exploração. Em engajamentos com EDR, prefira técnicas menos ruidosas
e contas de teste; coordene dumping com o cliente.

## Variante

- Variante LSA secrets / autologon: trato separado da família `win-cred`.

## Setup

Espelho do alvo. Sem WAF/EDR às vezes — anoto o delta.

## Fluxo

1. Verifico privilégios e políticas de credential guard.
2. Enumero stores não-LSASS primeiro (files, vault, scripts).
3. Se autorizado, avalio LSASS com método acordado.
4. Correlaciono credenciais com lateral movement.
5. Rotaciono segredos expostos após o teste.

## PoC mínimo

```powershell
# lab Windows — enum sem LSASS dump em prod
Get-Acl C:\ServicePath\svc.exe | Format-List
sc.exe qc SVC_lsa
# writable + priv service = privesc path tag 611dbd
```

## Pitfall

Dump de LSASS pode crashar hosts — com cautela.
Não exfiltro NTDS sem escopo de Domain Compromise explícito.

LOLBin: parent-child + linha de comando que o EDR deveria ter visto.

## Prova do lab

Tipo de credencial; host; uso em lateral (sem dumps completos).

## Refs

- [MITRE ATT&CK](https://attack.mitre.org/)
- [SpecterOps — DPAPI](https://posts.specterops.io/operational-guidance-for-offensive-user-dpapi-abuse-1fb7fac8b107)
- [MITRE ATT&CK T1003](https://attack.mitre.org/techniques/T1003/)

## Relacionadas

- [LSA secrets / autologon](0244-win-cred-lsa.md)
- [browser saved passwords](0247-win-cred-browser.md)
- [user/machine certs](0249-win-cred-cert.md)
- [DPAPI masterkey abuse](0242-win-cred-dpapi.md)
- [GPP/legacy secrets](0250-win-cred-gpp.md)