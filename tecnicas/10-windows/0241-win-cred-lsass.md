---
id: "0241"
categoria: "10-windows"
familia: "win-cred"
slug: "lsass"
angulo: "base"
mitre: "T1003"
owasp: ""
tags: ["10-windows", "win-cred", "base", "t1003"]
aliases: ["LSASS dump (autorizado)", "lsass"]
---

# LSASS dump (autorizado)

**Credential access** · `T1003 / T1555 / T1552`

## Contexto

LSASS dump, DPAPI, Credential Manager, LSA secrets, certificates e browser stores
são fontes típicas pós-exploração. Em engajamentos com EDR, prefira técnicas menos ruidosas
e contas de teste; coordene dumping com o cliente.

## Como eu faço

1. Verifico privilégios e políticas de credential guard.
2. Enumero stores não-LSASS primeiro (files, vault, scripts).
3. Se autorizado, avalio LSASS com método acordado.
4. Correlaciono credenciais com lateral movement.
5. Rotaciono segredos expostos após o teste.

## PoC mínimo

```powershell
# lab Windows — enum sem LSASS dump em prod
Get-Acl C:\ServicePath\svc.exe | Format-List
sc.exe qc SVC_lsass
# writable + priv service = privesc path tag 5d900b
```

## Diferencial desta nota

- **Método + detecção** — muda ruído e o que entra no PDF.

Antes de Critical em LSASS dump autorizado, confiro se a telemetria que eu cobraria reagiria — EDR LSASS access; Sysmon 10; Credential Guard.

## Onde já errei

Dump de LSASS pode crashar hosts — com cautela.
Não exfiltro NTDS sem escopo de Domain Compromise explícito.

DLL/serviço: path writable + binário sob identidade privilegiada. Sem os dois, não é privesc.

## Entrega

- blue: EDR LSASS access; Sysmon 10; Credential Guard.
- fix: Credential Guard; LAPS; gMSA; proibir debug privileges; vault hygiene.
- proof: Tipo de credencial; host; uso em lateral (sem dumps completos).

## Refs

- [MITRE ATT&CK T1003](https://attack.mitre.org/techniques/T1003/)
- [MITRE ATT&CK T1555](https://attack.mitre.org/techniques/T1555/)
- [MITRE ATT&CK T1552](https://attack.mitre.org/techniques/T1552/)
- [MITRE ATT&CK](https://attack.mitre.org/)
- [SpecterOps — DPAPI](https://posts.specterops.io/operational-guidance-for-offensive-user-dpapi-abuse-1fb7fac8b107)

## Relacionadas

- [LSASS dump (autorizado) — lab](0621-win-cred-lsass--lab.md)
- [browser saved passwords](0247-win-cred-browser.md)
- [user/machine certs](0249-win-cred-cert.md)
- [DPAPI masterkey abuse](0242-win-cred-dpapi.md)
- [GPP/legacy secrets](0250-win-cred-gpp.md)
- [Direitos de DCSync (path)](../09-ad/0213-ad-dacl-dcsync.md)
- [NTDS.dit (escopo DC) (path)](0246-win-cred-ntds.md)