# MITM IPv6 (mitm6)

**Network misconfig** · `T1557 Adversary-in-the-Middle`

## Contexto

Em redes Windows internas, LLMNR/NBT-NS poisoning captura hashes NetNTLMv2 e possibilita
SMB/HTTP relay para tomada de conta ou execução, dependendo de signing e LDAP protections.
É um dos caminhos mais realistas em AD interno — mas exige autorização de MitM.

## O que muda aqui

- Se não validar **DHCPv6 spoof**, a nota fica genérica.
- Signing/EPA/channel binding decidem se o relay vive.

## Como testo

1. Confirmar ROE para poisoning na VLAN.
2. Identifico broadcast name resolution ativa.
3. Capturo challenges com responder/inveigh **autorizado**.
4. Avalio relay para SMB/LDAP/HTTP com signing off.
5. Relatar hosts sem signing e contas privilegiadas expostas.

## PoC mínimo

```bash
# relay lab — segmento acordado, conta teste
ntlmrelayx.py -t smb://TARGET.lab.local -smb2support --no-dump
# trigger ipv6; evidência: auth USER_A + ação não destrutiva tag 2dbe8d
```

## Campo

Responder/ntlmrelayx em segmento acordado — sem poisoning do floor inteiro.

Falso amigo em MITM IPv6 (mitm6): UI/log gritam, impacto não. Exijo Detectar Rogue WPAD/LLMNR responders.

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

- MITRE T1557.001
- SpecterOps AD guides