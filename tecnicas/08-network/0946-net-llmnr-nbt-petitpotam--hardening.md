---
id: "0946"
categoria: "08-network"
familia: "net-llmnr-nbt"
slug: "petitpotam"
angulo: "hardening"
mitre: "T1557"
owasp: ""
tags: ["08-network", "net-llmnr-nbt", "hardening", "t1557"]
aliases: ["coerção + relay", "petitpotam", "petitpotam-hardening"]
---

# coerção + relay — hardening

Do PoC ao controle — coerção + relay.

## Risco

Em redes Windows internas, LLMNR/NBT-NS poisoning captura hashes NetNTLMv2 e possibilita
SMB/HTTP relay para tomada de conta ou execução, dependendo de signing e LDAP protections.
É um dos caminhos mais realistas em AD interno — mas exige autorização de MitM.

## Controles desta variante

- **Somente lab/autorizado** — muda ruído e o que entra no PDF.
- Signing/EPA/channel binding decidem se o relay vive.

## Camadas

Controle que fecha: Desabilitar LLMNR/NBT-NS; SMB signing obrigatório; LDAP signing/channel binding;
EPA; Network access control.
Sinal que deveria existir: Detectar Rogue WPAD/LLMNR responders; SMB signing compliance.

## No lab ficou assim

```bash
# verificação pós-hardening petitpotam
curl -sk -o /dev/null -w '%{http_code}\n' https://app.lab.local/petitpotam/10042 \
  -H 'Cookie: session=USER_B'
# esperado 403 — tag 1a5772
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

- [coerção + relay](0186-net-llmnr-nbt-petitpotam.md)
- [coerção + relay — lab](0566-net-llmnr-nbt-petitpotam--lab.md)
- [crack NetNTLMv2 de conta teste](0188-net-llmnr-nbt-crack.md)
- [detecção purple](0189-net-llmnr-nbt-detect.md)
- [coerção EFS](0187-net-llmnr-nbt-efs.md)
- [playbook de hardening GPO](0190-net-llmnr-nbt-hardening.md)
- [AD CS ESC8 (relay HTTP) (path)](../09-ad/0227-ad-cs-esc8.md)
- [Direitos de DCSync (path)](../09-ad/0213-ad-dacl-dcsync.md)