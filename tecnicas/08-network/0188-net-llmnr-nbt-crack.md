---
id: "0188"
categoria: "08-network"
familia: "net-llmnr-nbt"
slug: "crack"
angulo: "base"
mitre: "T1557"
owasp: ""
tags: ["08-network", "net-llmnr-nbt", "base", "t1557"]
aliases: ["crack NetNTLMv2 de conta teste", "crack"]
---

# crack NetNTLMv2 de conta teste

**Network misconfig** · `T1557 Adversary-in-the-Middle`

## Contexto

Em redes Windows internas, LLMNR/NBT-NS poisoning captura hashes NetNTLMv2 e possibilita
SMB/HTTP relay para tomada de conta ou execução, dependendo de signing e LDAP protections.
É um dos caminhos mais realistas em AD interno — mas exige autorização de MitM.

## O que muda aqui

- **Hashcat offline ético** — muda ruído e o que entra no PDF.
- Signing/EPA/channel binding decidem se o relay vive.

## Como testo

1. Confirmar ROE para poisoning na VLAN.
2. Identifico broadcast name resolution ativa.
3. Capturo challenges com responder/inveigh **autorizado**.
4. Avalio relay para SMB/LDAP/HTTP com signing off.
5. Relatar hosts sem signing e contas privilegiadas expostas.

## Sinal / query

```bash
# relay lab — segmento acordado, conta teste
ntlmrelayx.py -t smb://TARGET.lab.local -smb2support --no-dump
# trigger crack; evidência: auth USER_A + ação não destrutiva tag 235e0c
```

## Campo

Mensuro SMB/LDAP signing e EPA antes de montar relay. Sem isso o path é teatro.

Antes de Critical em crack NetNTLMv2 de conta teste, confiro se a telemetria que eu cobraria reagiria — Detectar Rogue WPAD/LLMNR responders; SMB signing compliance.

## Já me queimei

Poisoning afeta performance e pode capturar usuários reais — isole VLAN de teste se possível.
Não cracke hashes de usuários reais fora da política.

## Blue

- Detectar: Detectar Rogue WPAD/LLMNR responders; SMB signing compliance.
- Fechar: Desabilitar LLMNR/NBT-NS; SMB signing obrigatório; LDAP signing/channel binding;
EPA; Network access control.

## Evidência

Hash de conta de teste / relay success; GPO recomendada.

## Refs

- [MITRE ATT&CK T1557](https://attack.mitre.org/techniques/T1557/)
- [MITRE ATT&CK T1557.001](https://attack.mitre.org/techniques/T1557/001/)
- [SpecterOps — AD security](https://posts.specterops.io/)
- [HackTricks — LLMNR/NBT-NS spoofing](https://book.hacktricks.xyz/generic-methodologies-and-resources/pentesting-network/spoofing-llmnr-nbt-ns-mdns-dns-and-wpad-and-relay-attacks)

## Relacionadas

- [crack NetNTLMv2 de conta teste — lab](0568-net-llmnr-nbt-crack--lab.md)
- [crack NetNTLMv2 de conta teste — hardening](0948-net-llmnr-nbt-crack--hardening.md)
- [detecção purple](0189-net-llmnr-nbt-detect.md)
- [coerção EFS](0187-net-llmnr-nbt-efs.md)
- [playbook de hardening GPO](0190-net-llmnr-nbt-hardening.md)
- [HTTP → LDAP relay](0183-net-llmnr-nbt-http-relay.md)