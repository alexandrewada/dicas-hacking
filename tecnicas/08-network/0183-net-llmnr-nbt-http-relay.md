# HTTP → LDAP relay

## Contexto

Em redes Windows internas, LLMNR/NBT-NS poisoning captura hashes NetNTLMv2 e possibilita
SMB/HTTP relay para tomada de conta ou execução, dependendo de signing e LDAP protections.
É um dos caminhos mais realistas em AD interno — mas exige autorização de MitM.

## Detalhe

- **AD CS web enrollment** — muda ruído e o que entra no PDF.
- Signing/EPA/channel binding decidem se o relay vive.

## Execução

1. Confirmar ROE para poisoning na VLAN.
2. Identifico broadcast name resolution ativa.
3. Capturo challenges com responder/inveigh **autorizado**.
4. Avalio relay para SMB/LDAP/HTTP com signing off.
5. Relatar hosts sem signing e contas privilegiadas expostas.

## No lab ficou assim

```bash
# relay lab — segmento acordado, conta teste
ntlmrelayx.py -t smb://TARGET.lab.local -smb2support --no-dump
# trigger http-relay; evidência: auth USER_A + ação não destrutiva tag 7ffa34
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

- MITRE T1557.001
- SpecterOps AD guides