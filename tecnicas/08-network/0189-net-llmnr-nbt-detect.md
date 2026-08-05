---
id: "0189"
categoria: "08-network"
familia: "net-llmnr-nbt"
slug: "detect"
angulo: "base"
mitre: ""
owasp: ""
tags: ["08-network", "net-llmnr-nbt", "base"]
aliases: ["detecção purple", "detect"]
---

# detecção purple

## Contexto

Em redes Windows internas, LLMNR/NBT-NS poisoning captura hashes NetNTLMv2 e possibilita
SMB/HTTP relay para tomada de conta ou execução, dependendo de signing e LDAP protections.
É um dos caminhos mais realistas em AD interno — mas exige autorização de MitM.

## Detalhe

- Detalhe que pago pra ver: **Eventos e network IDS**.
- Signing/EPA/channel binding decidem se o relay vive.

## Execução

1. Confirmar ROE para poisoning na VLAN.
2. Identifico broadcast name resolution ativa.
3. Capturo challenges com responder/inveigh **autorizado**.
4. Avalio relay para SMB/LDAP/HTTP com signing off.
5. Relatar hosts sem signing e contas privilegiadas expostas.

## Exemplo

```bash
# relay lab — segmento acordado, conta teste
ntlmrelayx.py -t smb://TARGET.lab.local -smb2support --no-dump
# trigger detect; evidência: auth USER_A + ação não destrutiva tag 8f033d
```

## OpSec

Poisoning afeta performance e pode capturar usuários reais — isole VLAN de teste se possível.

## Cuidados

Poisoning afeta performance e pode capturar usuários reais — isole VLAN de teste se possível.
Não cracke hashes de usuários reais fora da política.

## Fechamento

| | |
|---|---|
| Detecção | Detectar Rogue WPAD/LLMNR responders; SMB signing compliance. |
| Remediação | Desabilitar LLMNR/NBT-NS; SMB signing obrigatório; LDAP signing/channel binding;
EPA; Network access control. |
| Evidência | Hash de conta de teste / relay success; GPO recomendada. |

## Refs

- [MITRE ATT&CK T1557.001](https://attack.mitre.org/techniques/T1557/001/)
- [SpecterOps — AD security](https://posts.specterops.io/)
- [HackTricks — LLMNR/NBT-NS spoofing](https://book.hacktricks.xyz/generic-methodologies-and-resources/pentesting-network/spoofing-llmnr-nbt-ns-mdns-dns-and-wpad-and-relay-attacks)

## Relacionadas

- [detecção purple — lab](0569-net-llmnr-nbt-detect--lab.md)
- [detecção purple — hardening](0949-net-llmnr-nbt-detect--hardening.md)
- [crack NetNTLMv2 de conta teste](0188-net-llmnr-nbt-crack.md)
- [coerção EFS](0187-net-llmnr-nbt-efs.md)
- [playbook de hardening GPO](0190-net-llmnr-nbt-hardening.md)
- [HTTP → LDAP relay](0183-net-llmnr-nbt-http-relay.md)