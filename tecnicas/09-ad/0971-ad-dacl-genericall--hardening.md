# GenericAll em usuário/grupo — hardening

Do PoC ao controle — GenericAll em usuário/grupo.

## Risco

BloodHound popularizou edges: GenericAll, WriteDACL, ForceChangePassword, DCSync rights,
AddMember, etc. valida o caminho em lab controlado e prova com ação mínima
(reset de conta teste, add a grupo lab), não com destruição.

## Controles desta variante

- Detalhe que pago pra ver: **Takeover direto**.

## Camadas

1) Bloqueio imediato
2) Directory Services Changes auditing; BloodHound Enterprise-like monitoring.
3) AdminSDHolder higiene; least privilege; Privileged Access Workstations;
remover ACEs excessivos.
Reteste com o mesmo PoC — critério: a prova desta variante falha.

## Exemplo

```text
checklist genericall:
- [ ] controle preventivo ativo
- [ ] telemetria cobre o PoC
- [ ] reteste com mesma prova (ad0286) falha
```

## Armadilha

DCSync em produção é sensível — alinhe com cliente.
Evito resetar senhas de usuários reais.

## Antes/depois

Edge BloodHound; PoC controlado; ACE dump.

Aceite de risco só por escrito, com prazo.

## Refs

- SpecterOps BloodHound docs
- MITRE AD techniques