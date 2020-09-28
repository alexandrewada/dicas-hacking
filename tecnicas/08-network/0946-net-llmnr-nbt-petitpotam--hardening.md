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

- MITRE T1557.001
- SpecterOps AD guides