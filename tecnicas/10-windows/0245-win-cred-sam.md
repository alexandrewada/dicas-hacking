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

Refs: MITRE Credential Access, SpecterOps DPAPI