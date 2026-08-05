---
id: "0245"
categoria: "10-windows"
familia: "win-cred"
slug: "sam"
angulo: "base"
mitre: "T1003"
owasp: ""
tags: ["10-windows", "win-cred", "base", "t1003"]
aliases: ["SAM local dump", "sam"]
---

# SAM local dump

**Credential access** · `T1003 / T1555 / T1552`

LSASS dump, DPAPI, Credential Manager, LSA secrets, certificates e browser stores
são fontes típicas pós-exploração. Em engajamentos com EDR, prefira técnicas menos ruidosas
e contas de teste; coordene dumping com o cliente.

**Variante:** Detalhe que pago pra ver: **Se admin local**.

**Método**

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
# writable + priv service = privesc path tag ffc726
```

**Freio:** Dump de LSASS pode crashar hosts — com cautela.

Falso amigo em SAM local dump: UI/log gritam, impacto não. Exijo EDR LSASS access.

Detecto via: EDR LSASS access; Sysmon 10; Credential Guard.

Corrijo com: Credential Guard; LAPS; gMSA; proibir debug privileges; vault hygiene.

Levo no report: Tipo de credencial; host; uso em lateral (sem dumps completos).

## Refs

- [MITRE ATT&CK T1003](https://attack.mitre.org/techniques/T1003/)
- [MITRE ATT&CK T1555](https://attack.mitre.org/techniques/T1555/)
- [MITRE ATT&CK T1552](https://attack.mitre.org/techniques/T1552/)
- [MITRE ATT&CK](https://attack.mitre.org/)
- [SpecterOps — DPAPI](https://posts.specterops.io/operational-guidance-for-offensive-user-dpapi-abuse-1fb7fac8b107)

## Relacionadas

- [SAM local dump — lab](0625-win-cred-sam--lab.md)
- [browser saved passwords](0247-win-cred-browser.md)
- [user/machine certs](0249-win-cred-cert.md)
- [DPAPI masterkey abuse](0242-win-cred-dpapi.md)
- [GPP/legacy secrets](0250-win-cred-gpp.md)