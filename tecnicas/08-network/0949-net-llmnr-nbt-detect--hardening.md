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

- MITRE T1557.001
- SpecterOps AD guides