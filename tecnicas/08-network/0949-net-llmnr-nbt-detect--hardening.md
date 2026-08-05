---
id: "0949"
categoria: "08-network"
familia: "net-llmnr-nbt"
slug: "detect"
angulo: "hardening"
mitre: ""
owasp: ""
tags: ["08-network", "net-llmnr-nbt", "hardening"]
aliases: ["detecção purple", "detect", "detect-hardening"]
---

# detecção purple — hardening

Do PoC ao controle — detecção purple.

## Risco

Em redes Windows internas, LLMNR/NBT-NS poisoning captura hashes NetNTLMv2 e possibilita
SMB/HTTP relay para tomada de conta ou execução, dependendo de signing e LDAP protections.
É um dos caminhos mais realistas em AD interno — mas exige autorização de MitM.

## Controles desta variante

- Detalhe que pago pra ver: **Eventos e network IDS**.
- Signing/EPA/channel binding decidem se o relay vive.

## Camadas

Hotfix: quebra a exploração direta de detecção purple.
Detectivo: Detectar Rogue WPAD/LLMNR responders; SMB signing compliance.
Estrutural: Desabilitar LLMNR/NBT-NS; SMB signing obrigatório; LDAP signing/channel binding;
EPA; Network access control.

## No lab ficou assim

```text
checklist detect:
- [ ] controle preventivo ativo
- [ ] telemetria cobre o PoC
- [ ] reteste com mesma prova (bcf6a2) falha
```

## Armadilha

Poisoning afeta performance e pode capturar usuários reais — isole VLAN de teste se possível.
Não cracke hashes de usuários reais fora da política.

## Antes/depois

Hash de conta de teste / relay success; GPO recomendada.

Aceite de risco só por escrito, com prazo.

## Refs

- [MITRE ATT&CK T1557.001](https://attack.mitre.org/techniques/T1557/001/)
- [SpecterOps — AD security](https://posts.specterops.io/)
- [HackTricks — LLMNR/NBT-NS spoofing](https://book.hacktricks.xyz/generic-methodologies-and-resources/pentesting-network/spoofing-llmnr-nbt-ns-mdns-dns-and-wpad-and-relay-attacks)

## Relacionadas

- [detecção purple](0189-net-llmnr-nbt-detect.md)
- [detecção purple — lab](0569-net-llmnr-nbt-detect--lab.md)
- [crack NetNTLMv2 de conta teste](0188-net-llmnr-nbt-crack.md)
- [coerção EFS](0187-net-llmnr-nbt-efs.md)
- [playbook de hardening GPO](0190-net-llmnr-nbt-hardening.md)
- [HTTP → LDAP relay](0183-net-llmnr-nbt-http-relay.md)