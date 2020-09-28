# MITM IPv6 (mitm6) — hardening

Do PoC ao controle — MITM IPv6 (mitm6).

## Risco

Em redes Windows internas, LLMNR/NBT-NS poisoning captura hashes NetNTLMv2 e possibilita
SMB/HTTP relay para tomada de conta ou execução, dependendo de signing e LDAP protections.
É um dos caminhos mais realistas em AD interno — mas exige autorização de MitM.

## Controles desta variante

- Se não validar **DHCPv6 spoof**, a nota fica genérica.
- Signing/EPA/channel binding decidem se o relay vive.

## Camadas

1) Bloqueio imediato
2) Detectar Rogue WPAD/LLMNR responders; SMB signing compliance.
3) Desabilitar LLMNR/NBT-NS; SMB signing obrigatório; LDAP signing/channel binding;
EPA; Network access control.
Reteste com o mesmo PoC — critério: a prova desta variante falha.

## No lab ficou assim

```bash
# verificação pós-hardening ipv6
curl -sk -o /dev/null -w '%{http_code}\n' https://app.lab.local/ipv6/a1b2c3d4-e5f6-7890-abcd-ef1234567890 \
  -H 'Cookie: session=USER_B'
# esperado 403 — tag dbe9de
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