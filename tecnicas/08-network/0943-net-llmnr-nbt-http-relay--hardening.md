---
id: "0943"
categoria: "08-network"
familia: "net-llmnr-nbt"
slug: "http-relay"
angulo: "hardening"
mitre: ""
owasp: ""
tags: ["08-network", "net-llmnr-nbt", "hardening"]
aliases: ["HTTP → LDAP relay", "http-relay", "http-relay-hardening"]
---

# HTTP → LDAP relay — hardening

Do PoC ao controle — HTTP → LDAP relay.

## Risco

Em redes Windows internas, LLMNR/NBT-NS poisoning captura hashes NetNTLMv2 e possibilita
SMB/HTTP relay para tomada de conta ou execução, dependendo de signing e LDAP protections.
É um dos caminhos mais realistas em AD interno — mas exige autorização de MitM.

## Controles desta variante

- **AD CS web enrollment** — muda ruído e o que entra no PDF.
- Signing/EPA/channel binding decidem se o relay vive.

## Camadas

Hotfix: quebra a exploração direta de HTTP → LDAP relay.
Detectivo: Detectar Rogue WPAD/LLMNR responders; SMB signing compliance.
Estrutural: Desabilitar LLMNR/NBT-NS; SMB signing obrigatório; LDAP signing/channel binding;
EPA; Network access control.

## Exemplo

```text
antes: controle ausente para http-relay
depois: ownership check / deny default em TARGET
verificação: PoC 954ddd retorna 403/blocked
reteste USER_A vs USER_B
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

- [HTTP → LDAP relay](0183-net-llmnr-nbt-http-relay.md)
- [HTTP → LDAP relay — lab](0563-net-llmnr-nbt-http-relay--lab.md)
- [crack NetNTLMv2 de conta teste](0188-net-llmnr-nbt-crack.md)
- [detecção purple](0189-net-llmnr-nbt-detect.md)
- [coerção EFS](0187-net-llmnr-nbt-efs.md)
- [playbook de hardening GPO](0190-net-llmnr-nbt-hardening.md)