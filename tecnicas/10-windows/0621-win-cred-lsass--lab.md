# LSASS dump (autorizado) — lab

Critério: outro analista fecha sozinho com esta nota.

## Contexto

LSASS dump, DPAPI, Credential Manager, LSA secrets, certificates e browser stores
são fontes típicas pós-exploração. Em engajamentos com EDR, prefira técnicas menos ruidosas
e contas de teste; coordene dumping com o cliente.

## Variante

- **Método + detecção** — muda ruído e o que entra no PDF.

## Setup

Espelho do alvo. Sem WAF/EDR às vezes — anoto o delta.

## Fluxo

1. Verifico privilégios e políticas de credential guard.
2. Enumero stores não-LSASS primeiro (files, vault, scripts).
3. Se autorizado, avalio LSASS com método acordado.
4. Correlaciono credenciais com lateral movement.
5. Rotaciono segredos expostos após o teste.

## Exemplo

```powershell
# lab Windows — enum sem LSASS dump em prod
Get-Acl C:\ServicePath\svc.exe | Format-List
sc.exe qc SVC_lsass
# writable + priv service = privesc path tag 5f76af
```

## Pitfall

Dump de LSASS pode crashar hosts — com cautela.
Não exfiltro NTDS sem escopo de Domain Compromise explícito.

DLL/serviço: path writable + binário sob identidade privilegiada. Sem os dois, não é privesc.

## Prova do lab

Tipo de credencial; host; uso em lateral (sem dumps completos).

## Refs

- MITRE Credential Access
- SpecterOps DPAPI