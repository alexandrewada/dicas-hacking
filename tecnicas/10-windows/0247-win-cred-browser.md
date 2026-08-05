---
id: "0247"
categoria: "10-windows"
familia: "win-cred"
slug: "browser"
angulo: "base"
mitre: "T1003"
owasp: ""
tags: ["10-windows", "win-cred", "base", "t1003"]
aliases: ["browser saved passwords", "browser"]
---

# browser saved passwords

**Credential access** · `T1003 / T1555 / T1552`

## Contexto

LSASS dump, DPAPI, Credential Manager, LSA secrets, certificates e browser stores
são fontes típicas pós-exploração. Em engajamentos com EDR, prefira técnicas menos ruidosas
e contas de teste; coordene dumping com o cliente.

## O que muda aqui

- Variante browser saved passwords: trato separado da família `win-cred`.

## Como testo

1. Verifico privilégios e políticas de credential guard.
2. Enumero stores não-LSASS primeiro (files, vault, scripts).
3. Se autorizado, avalio LSASS com método acordado.
4. Correlaciono credenciais com lateral movement.
5. Rotaciono segredos expostos após o teste.

## No lab ficou assim

```powershell
# lab Windows — enum sem LSASS dump em prod
Get-Acl C:\ServicePath\svc.exe | Format-List
sc.exe qc SVC_browser
# writable + priv service = privesc path tag a36d5a
```

## Campo

DLL/serviço: path writable + binário sob identidade privilegiada. Sem os dois, não é privesc.

Antes de Critical em browser saved passwords, confiro se a telemetria que eu cobraria reagiria — EDR LSASS access; Sysmon 10; Credential Guard.

## Já me queimei

Dump de LSASS pode crashar hosts — com cautela.
Não exfiltro NTDS sem escopo de Domain Compromise explícito.

## Blue

- Detectar: EDR LSASS access; Sysmon 10; Credential Guard.
- Fechar: Credential Guard; LAPS; gMSA; proibir debug privileges; vault hygiene.

## Evidência

Tipo de credencial; host; uso em lateral (sem dumps completos).

## Refs

- [MITRE ATT&CK T1003](https://attack.mitre.org/techniques/T1003/)
- [MITRE ATT&CK T1555](https://attack.mitre.org/techniques/T1555/)
- [MITRE ATT&CK T1552](https://attack.mitre.org/techniques/T1552/)
- [MITRE ATT&CK](https://attack.mitre.org/)
- [SpecterOps — DPAPI](https://posts.specterops.io/operational-guidance-for-offensive-user-dpapi-abuse-1fb7fac8b107)

## Relacionadas

- [browser saved passwords — lab](0627-win-cred-browser--lab.md)
- [user/machine certs](0249-win-cred-cert.md)
- [DPAPI masterkey abuse](0242-win-cred-dpapi.md)
- [GPP/legacy secrets](0250-win-cred-gpp.md)
- [LSA secrets / autologon](0244-win-cred-lsa.md)