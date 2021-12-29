# Credential Manager

**Credential access** · `T1003 / T1555 / T1552`

## Contexto

LSASS dump, DPAPI, Credential Manager, LSA secrets, certificates e browser stores
são fontes típicas pós-exploração. Em engajamentos com EDR, prefira técnicas menos ruidosas
e contas de teste; coordene dumping com o cliente.

## O que muda aqui

- Variante Credential Manager: trato separado da família `win-cred`.

## Como testo

1. Verifico privilégios e políticas de credential guard.
2. Enumero stores não-LSASS primeiro (files, vault, scripts).
3. Se autorizado, avalio LSASS com método acordado.
4. Correlaciono credenciais com lateral movement.
5. Rotaciono segredos expostos após o teste.

## PoC mínimo

```powershell
# lab Windows — enum sem LSASS dump em prod
Get-Acl C:\ServicePath\svc.exe | Format-List
sc.exe qc SVC_vault
# writable + priv service = privesc path tag a0af26
```

## Campo

LOLBin: parent-child + linha de comando que o EDR deveria ter visto.

Credential Manager: se não reproduz efeito (authz/dado/exec), não infla severidade. Referência de sinal: EDR LSASS access; Sysmon 10; Credential Guard.

## Já me queimei

Dump de LSASS pode crashar hosts — com cautela.
Não exfiltro NTDS sem escopo de Domain Compromise explícito.

## Blue

- Detectar: EDR LSASS access; Sysmon 10; Credential Guard.
- Fechar: Credential Guard; LAPS; gMSA; proibir debug privileges; vault hygiene.

## Evidência

Tipo de credencial; host; uso em lateral (sem dumps completos).

## Refs

- MITRE Credential Access
- SpecterOps DPAPI