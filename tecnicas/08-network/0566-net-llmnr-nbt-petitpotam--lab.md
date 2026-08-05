---
id: "0566"
categoria: "08-network"
familia: "net-llmnr-nbt"
slug: "petitpotam"
angulo: "lab"
mitre: "T1557"
owasp: ""
tags: ["08-network", "net-llmnr-nbt", "lab", "t1557"]
aliases: ["coerção + relay", "petitpotam", "petitpotam-lab"]
---

# coerção + relay — lab

Critério: outro analista fecha sozinho com esta nota.

## Contexto

Em redes Windows internas, LLMNR/NBT-NS poisoning captura hashes NetNTLMv2 e possibilita
SMB/HTTP relay para tomada de conta ou execução, dependendo de signing e LDAP protections.
É um dos caminhos mais realistas em AD interno — mas exige autorização de MitM.

## Variante

- **Somente lab/autorizado** — muda ruído e o que entra no PDF.
- Signing/EPA/channel binding decidem se o relay vive.

## Setup

Espelho do alvo. Sem WAF/EDR às vezes — anoto o delta.

## Fluxo

1. Confirmar ROE para poisoning na VLAN.
2. Identifico broadcast name resolution ativa.
3. Capturo challenges com responder/inveigh **autorizado**.
4. Avalio relay para SMB/LDAP/HTTP com signing off.
5. Relatar hosts sem signing e contas privilegiadas expostas.

## PoC mínimo

```bash
# relay lab — segmento acordado, conta teste
ntlmrelayx.py -t smb://TARGET.lab.local -smb2support --no-dump
# trigger petitpotam; evidência: auth USER_A + ação não destrutiva tag 3dd91d
```

## Pitfall

Poisoning afeta performance e pode capturar usuários reais — isole VLAN de teste se possível.
Não cracke hashes de usuários reais fora da política.

Mensuro SMB/LDAP signing e EPA antes de montar relay. Sem isso o path é teatro.

## Prova do lab

Hash de conta de teste / relay success; GPO recomendada.

## Refs

- [MITRE ATT&CK T1557](https://attack.mitre.org/techniques/T1557/)
- [MITRE ATT&CK T1557.001](https://attack.mitre.org/techniques/T1557/001/)
- [SpecterOps — AD security](https://posts.specterops.io/)
- [HackTricks — LLMNR/NBT-NS spoofing](https://book.hacktricks.xyz/generic-methodologies-and-resources/pentesting-network/spoofing-llmnr-nbt-ns-mdns-dns-and-wpad-and-relay-attacks)

## Relacionadas

- [coerção + relay](0186-net-llmnr-nbt-petitpotam.md)
- [coerção + relay — hardening](0946-net-llmnr-nbt-petitpotam--hardening.md)
- [crack NetNTLMv2 de conta teste](0188-net-llmnr-nbt-crack.md)
- [detecção purple](0189-net-llmnr-nbt-detect.md)
- [coerção EFS](0187-net-llmnr-nbt-efs.md)
- [playbook de hardening GPO](0190-net-llmnr-nbt-hardening.md)
- [AD CS ESC8 (relay HTTP) (path)](../09-ad/0227-ad-cs-esc8.md)
- [Direitos de DCSync (path)](../09-ad/0213-ad-dacl-dcsync.md)