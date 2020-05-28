# relay para LDAP

## Leitura rápida

Em redes Windows internas, LLMNR/NBT-NS poisoning captura hashes NetNTLMv2 e possibilita
SMB/HTTP relay para tomada de conta ou execução, dependendo de signing e LDAP protections.
É um dos caminhos mais realistas em AD interno — mas exige autorização de MitM.

## Foco

- **Criação de machine account se possível** — muda ruído e o que entra no PDF.
- Signing/EPA/channel binding decidem se o relay vive.

## Mãos na massa

1. Confirmar ROE para poisoning na VLAN.
2. Identifico broadcast name resolution ativa.
3. Capturo challenges com responder/inveigh **autorizado**.
4. Avalio relay para SMB/LDAP/HTTP com signing off.
5. Relatar hosts sem signing e contas privilegiadas expostas.

## Sinal / query

```bash
# relay lab — segmento acordado, conta teste
ntlmrelayx.py -t smb://TARGET.lab.local -smb2support --no-dump
# trigger ldap-relay; evidência: auth USER_A + ação não destrutiva tag ae21e2
```

Mensuro SMB/LDAP signing e EPA antes de montar relay. Sem isso o path é teatro.

## Pitfall

Poisoning afeta performance e pode capturar usuários reais — isole VLAN de teste se possível.
Não cracke hashes de usuários reais fora da política.

## Detecção / remediação

Detectar Rogue WPAD/LLMNR responders; SMB signing compliance.

→ Desabilitar LLMNR/NBT-NS; SMB signing obrigatório; LDAP signing/channel binding;
EPA; Network access control.

## Prova

Hash de conta de teste / relay success; GPO recomendada.

## Refs

- MITRE T1557.001
- SpecterOps AD guides