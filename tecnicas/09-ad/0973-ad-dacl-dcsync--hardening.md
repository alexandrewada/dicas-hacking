# Direitos de DCSync — hardening

Do PoC ao controle — Direitos de DCSync.

## Risco

BloodHound popularizou edges: GenericAll, WriteDACL, ForceChangePassword, DCSync rights,
AddMember, etc. valida o caminho em lab controlado e prova com ação mínima
(reset de conta teste, add a grupo lab), não com destruição.

## Controles desta variante

- Se não validar **Credential dump path**, a nota fica genérica.
- GetChanges/GetChangesAll em conta que não deveria ter — não em DA óbvio.

## Camadas

Hotfix: quebra a exploração direta de Direitos de DCSync.
Detectivo: Directory Services Changes auditing; BloodHound Enterprise-like monitoring.
Estrutural: AdminSDHolder higiene; least privilege; Privileged Access Workstations;
remover ACEs excessivos.

## PoC mínimo

```text
checklist dcsync:
- [ ] controle preventivo ativo
- [ ] telemetria cobre o PoC
- [ ] reteste com mesma prova (7548c0) falha
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