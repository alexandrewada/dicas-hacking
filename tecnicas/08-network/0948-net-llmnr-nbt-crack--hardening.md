---
id: "0948"
categoria: "08-network"
familia: "net-llmnr-nbt"
slug: "crack"
angulo: "hardening"
mitre: "T1557"
owasp: ""
tags: ["08-network", "net-llmnr-nbt", "hardening", "t1557"]
aliases: ["crack NetNTLMv2 de conta teste", "crack", "crack-hardening"]
---

# crack NetNTLMv2 de conta teste — hardening

Do PoC ao controle — crack NetNTLMv2 de conta teste.

## Risco

Em redes Windows internas, LLMNR/NBT-NS poisoning captura hashes NetNTLMv2 e possibilita
SMB/HTTP relay para tomada de conta ou execução, dependendo de signing e LDAP protections.
É um dos caminhos mais realistas em AD interno — mas exige autorização de MitM.

## Controles desta variante

- **Hashcat offline ético** — muda ruído e o que entra no PDF.
- Signing/EPA/channel binding decidem se o relay vive.

## Camadas

1) Bloqueio imediato
2) Detectar Rogue WPAD/LLMNR responders; SMB signing compliance.
3) Desabilitar LLMNR/NBT-NS; SMB signing obrigatório; LDAP signing/channel binding;
EPA; Network access control.
Reteste com o mesmo PoC — critério: a prova desta variante falha.

## PoC mínimo

```text
antes: controle ausente para crack
depois: ownership check / deny default em TARGET
verificação: PoC 1feb56 retorna 403/blocked
reteste USER_A vs USER_B
```

## Armadilha

Poisoning afeta performance e pode capturar usuários reais — isole VLAN de teste se possível.
Não cracke hashes de usuários reais fora da política.

## Antes/depois

Hash de conta de teste / relay success; GPO recomendada.

Aceite de risco só por escrito, com prazo.

## Refs

- [MITRE ATT&CK T1557](https://attack.mitre.org/techniques/T1557/)
- [MITRE ATT&CK T1557.001](https://attack.mitre.org/techniques/T1557/001/)
- [SpecterOps — AD security](https://posts.specterops.io/)
- [HackTricks — LLMNR/NBT-NS spoofing](https://book.hacktricks.xyz/generic-methodologies-and-resources/pentesting-network/spoofing-llmnr-nbt-ns-mdns-dns-and-wpad-and-relay-attacks)

## Relacionadas

- [crack NetNTLMv2 de conta teste](0188-net-llmnr-nbt-crack.md)
- [crack NetNTLMv2 de conta teste — lab](0568-net-llmnr-nbt-crack--lab.md)
- [detecção purple](0189-net-llmnr-nbt-detect.md)
- [coerção EFS](0187-net-llmnr-nbt-efs.md)
- [playbook de hardening GPO](0190-net-llmnr-nbt-hardening.md)
- [HTTP → LDAP relay](0183-net-llmnr-nbt-http-relay.md)