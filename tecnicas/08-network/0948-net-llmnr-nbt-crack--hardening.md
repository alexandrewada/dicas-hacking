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

- MITRE T1557.001
- SpecterOps AD guides