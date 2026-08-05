---
id: "0630"
categoria: "10-windows"
familia: "win-cred"
slug: "gpp"
angulo: "evidencia"
mitre: ""
owasp: ""
tags: ["10-windows", "win-cred", "evidencia"]
aliases: ["GPP/legacy secrets", "gpp", "gpp-evidencia"]
---

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

- [MITRE ATT&CK](https://attack.mitre.org/)
- [SpecterOps — DPAPI](https://posts.specterops.io/operational-guidance-for-offensive-user-dpapi-abuse-1fb7fac8b107)
- [MITRE ATT&CK T1003](https://attack.mitre.org/techniques/T1003/)

## Relacionadas

- [GPP/legacy secrets](0250-win-cred-gpp.md)
- [browser saved passwords](0247-win-cred-browser.md)
- [user/machine certs](0249-win-cred-cert.md)
- [DPAPI masterkey abuse](0242-win-cred-dpapi.md)
- [LSA secrets / autologon](0244-win-cred-lsa.md)