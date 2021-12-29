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

- MITRE Credential Access
- SpecterOps DPAPI