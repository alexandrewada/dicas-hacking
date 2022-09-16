# GPP/legacy secrets — evidência

Pacote pra GPP/legacy secrets sobreviver peer review.

## Contexto

LSASS dump, DPAPI, Credential Manager, LSA secrets, certificates e browser stores
são fontes típicas pós-exploração. Em engajamentos com EDR, prefira técnicas menos ruidosas
e contas de teste; coordene dumping com o cliente.

## O que precisa aparecer

- Variante GPP/legacy secrets: trato separado da família `win-cred`.

## Checklist

- pré-condição
- request/comando
- efeito de negócio
- CVSS justificado
- remediação
- reteste path

## Mínimo que eu aceito

Tipo de credencial; host; uso em lateral (sem dumps completos).

## PoC mínimo

```text
--- evidência redigida ---
req: GET /…/10042 Cookie=USER_B
res: 200 body_len=412 fields=[email,role] # PII mascarada
impacto: leitura cross-user (gpp)
hash_prova: 4a347e
```

## Remediação junto

Credential Guard; LAPS; gMSA; proibir debug privileges; vault hygiene.

## Se purple

EDR LSASS access; Sysmon 10; Credential Guard.

## Armadilha

Dump de LSASS pode crashar hosts — com cautela.
Não exfiltro NTDS sem escopo de Domain Compromise explícito.

## Refs

- MITRE Credential Access
- SpecterOps DPAPI